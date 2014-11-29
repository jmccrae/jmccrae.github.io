<?php include '../header.html'; ?>
<div class="row col-lg-6 col-lg-offset-3">

<h1>Lexical Linked Data Case Study: ALPINO Treebank</h1>

<p>In this post, I will detail how to publish a linguistic resource as linked data from scratch. These instructions are based on a Linux server with apache2, but should apply to other server types as well. As a case study the <a href="http://www.let.rug.nl/vannoord/trees/">ALPINO Treebank</a> a treebank for Dutch in XML and released under the GPLv2, hence we can republish it in RDF as long as we make an attribution to the original authors.</p>

<p>We will start by obtaining the resource, decompressing it and removing the non-data folders</p>

<pre><code>wget http://www.let.rug.nl/~vannoord/ftp/AlpinoCDROM/AlpinoCDROM.tgz
tar xzvf AlpinoCDROM.tgz
rm -fr Clig/ Papers/ stylesheets/ thistle-2-0-1/ xmlmatch/
</code></pre>

<p>Next, we do a simple RDF conversion, starting with this simple <a href="http://www.gac-grid.de/project-products/Software/XML2RDF.html">XSLT processor</a> and we will use the <code>xsltproc</code> command to do it:</p>

<pre><code>
for file in *.xml
do 
  xsltproc xml2rdf3.xsl $file >$file.rdf
done
rename .xml.rdf .rdf *.xml.rdf
</code></pre>

<p>Now we simply create a new folder on our apache2 server and copy the result there</p>

<pre><code>
cd /var/www/lexinfo.net/htdocs/
mkdir -p corpora/alpino
cp -r ~/AlpinoCDROM corpora/alpino
chown -R apache:apache corpora/
</code></pre>

<p>And now we see that the data is available</p>

<img src="alpino1.png" width="100%"/>

<p>In fact, a linked data server is just a normal server that returns RDF data, we make a quick modification to the MIME types to make sure it returns the correct type in 
<code>/etc/apache2/modules.d/00_mod_mime.conf</code> (on my server, check your Linux Distros documentation) and then restart the server.</p>

<pre><code>
AddType application/rdf+xml .rdf
AddType text/turtle .ttl

# For type maps (negotiated resources):
AddHandler type-map var
</code></pre>

<p>We can check this works very simply as follows</p>

<pre><code>
jmccrae@greententacle ~/AlpinoCDROM $ curl -I -H "Accept: application/rdf+xml" http://lexinfo.net/corpora/alpino/cgn_exs/1.rdf
HTTP/1.1 200 OK
Date: Thu, 09 Aug 2012 19:13:58 GMT
Server: Apache
Last-Modified: Thu, 09 Aug 2012 19:12:38 GMT
ETag: "1c96013-6e9-4c6da02bdb580"
Accept-Ranges: bytes
Content-Length: 1769
Cache-Control: max-age=1209600
Expires: Thu, 23 Aug 2012 19:13:58 GMT
Content-Type: application/rdf+xml
</code></pre>

<p>So far, so good... the next step is to enable content negotiation, for Alpino we have an issue that the raw XML files are renamed without extension, therefore we move all these files to the extension .txt. Then in each file we create a document call .htaccess and add the following line to it.</p>

<pre><code>
Options +MultiViews
</code></pre>

<p>Now we test it and</p>

<pre><code>
jmccrae@greententacle ~ $ curl -I -H "Accept: application/rdf+xml" http://lexinfo.net/corpora/alpino/cgn_exs/1
HTTP/1.1 200 OK
Date: Thu, 09 Aug 2012 19:38:08 GMT
Server: Apache
Content-Location: 1.rdf
Vary: negotiate,accept
TCN: choice
Last-Modified: Thu, 09 Aug 2012 19:12:38 GMT
ETag: "1c96013-6e9-4c6da02bdb580;4c6da48d60b80"
Accept-Ranges: bytes
Content-Length: 1769
Cache-Control: max-age=1209600
Expires: Thu, 23 Aug 2012 19:38:08 GMT
Content-Type: application/rdf+xml
</code></pre>

<p>It works... Now to link it to something. Inspecting the data, there are three clear groups of categories in the corpus, &ldquo;cat&rdquo; for categories/phrase types, &ldquo;rel&rdquo; for dependency relations and &ldquo;pos&rdquo; for part-of-speech tags. Many of these can be aligned to a data category registry or linguistic ontology. I choose to provide alignments to <a href="http://www.isocat.org/">ISOcat</a> and to <a href="http://www.lexinfo.net/">LexInfo</a>. This was performed by creating an OWL ontology to describe the categories used in the resource, for example the following describes &ldquo;adverbs&rdquo; in ALPINO</p>

<pre><code>
<owl:NamedIndividual rdf:about="http://lexinfo.net/corpora/alpino/categories#adv">
   <rdf:type rdf:resource="http://lexinfo.net/corpora/alpino/categories#PartOfSpeech"/>
   <rdfs:label xml:lang="en">Adverb</rdfs:label>
   <dcr:datcat rdf:resource="http://www.isocat.org/datcat/DC-1232"/>
   <owl:sameAs rdf:resource="&lexinfo;adverb"/>
</owl:NamedIndividual>
</code></pre>

<p>Finally we modify the XSLT to use these new categories, in particular we modify the script at line 105 (green is new code), so that it generates a triple with a URI object as follows</p>

<code><pre>
<xsl:choose>
  <xsl:when test="name()='rel'">
    <cat:rel>
      <xsl:attribute name="rdf:resource">
        <xsl:value-of select="concat('http://lexinfo.net/corpora/alpino/categories#',.)"/>
      </xsl:attribute>
    </cat:rel>
  </xsl:when>
  <xsl:when test="name()='cat'">
    <cat:cat>
      <xsl:attribute name="rdf:resource">
        <xsl:value-of select="concat('http://lexinfo.net/corpora/alpino/categories#',.)"/>
      </xsl:attribute>
    </cat:cat>
  </xsl:when>
  <xsl:when test="name()='pos'">
    <cat:pos>
      <xsl:attribute name="rdf:resource">
        <xsl:value-of select="concat('http://lexinfo.net/corpora/alpino/categories#',.)"/>
      </xsl:attribute>
    </cat:pos>
  </xsl:when>
  <xsl:otherwise>
     <xsl:element name="{name()}" namespace="{$ns}">
       <xsl:value-of select="."/>
     </xsl:element>
   </xsl:otherwise>
 </xsl:choose>
</pre></code>

<p>We apply this and publish this and our ontology and have the first version of our linked data corpora.</p>

<p>Finally, I make the resource browsable by creating a zipped dump of all the data and a new index page</p>

<p>In <a href="alpino2">Part 2</a>, we set-up a SPARQL endpoint and register the resource with CKAN</p>

<p>Ontology File: <a href="http://lexinfo.net/corpora/alpino/categories.rdf">http://lexinfo.net/corpora/alpino/categories.rdf</a></p>

<p>XSLT File: <a href="http://lexinfo.net/corpora/alpino/alpino_xml2rdf3.xsl">http://lexinfo.net/corpora/alpino/alpino_xml2rdf3.xsl</a></p>
</div>
<?php include '../footer.html'; ?>
