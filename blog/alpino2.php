<?php include '../header.html'; ?>
<div class="row col-lg-9 col-lg-offset-3">
    
    <h1>Lexical Linked Data Case Study: ALPINO Treebank - Part 2</h1>

    <p>Following on from the <a href="alpino">previous post</p>, we will now create a SPARQL endpoint so that we can query the contents of the data. To do this we will use the light-weight engine <a href="http://4store.org/">4store</a>. The first task is to set up the task, on an Ubuntu based machine this is simply achieved with</p>

<pre><code>sudo apt-get install 4store</code></pre>

    <p>Otherwise it may be necessary to install it following the <a href="http://4store.org/trac/wiki/Install">instructions</a>.</p>

    <p>Once 4store is installed we simply create a database, set up the back-end and load all data</p>

    <pre><code>4s-backend-setup alpino
4s-backend alpino
for file in `find . -name \*.rdf` 
do fileBase=`echo $file | sed 's/\\.\/\(.*\)\..*/\1/' ` 
    4s-import alpino -v -a -m "http://lexinfo.net/corpora/alpino/$fileBase" $file 
done
</code></pre>

    <p>Note, as the RDF files made by the XSLT do not specify the URI we must be careful when loading the data that 4store uses the right URIs.</p>

    <p>Next we set-up the web connector at a random (firewalled) port</p>

<pre><code>4s-httpd alpino -p 8888</code></pre>

    <p>Now we need to make it available to the web, we will do this through a PHP script, as the default HTTP interface for 4store is not particularly user friendly</p>

    <img src="screenshot-from-2012-08-30-174817.png"/>

    <p>I wrote the following PHP script for this:</p>

    <pre><code>&lt;?php
if(!isset($_REQUEST["query"])) { ?&gt;
&lt;html&gt;
 &lt;head&gt;
 &lt;title&gt;ALPINO corpus query&lt;/title&gt;
 &lt;/head&gt;
 &lt;body&gt;
 &lt;form action="" method="get"&gt;
 &lt;label for="query"&gt;Query:&lt;/label&gt;&lt;br/&gt;
 &lt;textarea name="query" rows="5" cols="80"&gt;
PREFIX cat: &lt;http://lexinfo.net/corpora/alpino/categories#&gt; 
PREFIX rdf: &lt;http://www.w3.org/1999/02/22-rdf-syntax-ns#&gt;
SELECT * WHERE { ?s ?p ?o } LIMIT 10
&lt;/textarea&gt;&lt;br/&gt;
 &lt;input type="submit"/&gt;
 &lt;/form&gt;
 &lt;/body&gt;
&lt;/html&gt;
&lt;? } else {
$ch = curl_init();
$url = "http://localhost:8888/sparql/?query=" . urlencode($_REQUEST["query"]);
curl_setopt($ch, CURLOPT_URL, $url);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
$data = curl_exec($ch);
$code = curl_getinfo($ch,CURLINFO_HTTP_CODE);
if($code == 200) {
 header("Content-type: application/sparql-results+xml");
 echo $data;
} else {
 echo $data;
}
curl_close($ch);
}
?&gt;
</code></pre>

    <p>Now the final step is to register the resource with <a href="http://thedatahub.org/">CKAN</a>. To do this we simply go to the website, create a user account and fill in the form thus:</p>

    <img src="screenshot-from-2012-08-30-184546.png"/>

    <p>In particular we added the following URLs</p>

    <ul>
        <li>The welcome page: http://lexinfo.net/corpora/alpino/index.html</li>
        <li>The SPARQL endpoint: http://lexinfo.net/corpora/alpino/query.php</li>
        <li>The ZIP of files: http://lexinfo.net/corpora/alpino/alpino-rdf.zip</li>
        <li>An example page: http://lexinfo.net/corpora/alpino/123.rdf</li>
    </ul>

    <p>Finally we send a mail to the open linguistics list to announce the <a href="http://linguistics.okfn.org/">Open Linguistics Working Group</a>.
</div>
<?php include '../footer.html'; ?>
