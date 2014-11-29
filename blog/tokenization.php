<?php include '../header.html'; ?>
<div class="row">
<h1>A simple regular expression for tokenization of (most) natural language</h1>

<p>I often need to tokenize text and have generally relied on the following fairly simple regular expression to do the trick</p>

<pre><code>
string.split("\\s+")
</code></pre>

<p><code>\\s</code> is the group for (ASCII) spaces and so while this works, in fact it quickly leads to problems, let's take an example bit of text</p>

<p>So in &ldquo;this test&rdquo;, we wish to check tokenization; among other things. So..., we ask a question? A make a statement statement! (and maybe a note). I'll check some other stuff, like we may have&nbsp;&nbsp;&nbsp;exagerated&nbps;&nbsp;&nbsp;spacing! Or strange quotes, like &laquo;en fran&ccedil;ais&raquo; or &#x84;auf Deutsch&#x93;.</p>

<P>So we quickly have the issue that we get tokens like <b>&ldquo;this</b> or <b>test&rdquo;</b>  that are not so good.. instead we would like to have the quotation marks as a token by themselves. Now there is a regular expression we could use:</p>

<pre><code>
string.split("\\b")
</code></pre>

<p>However, this creates it's own issues: firstly now each space is its own token and compound punctuations doesn't work, &ldquo;like in quotes<b>.&rdquo;</b> Even worse, contractions like &ldquo;doesn't&rdquo; get split into three tokens. Not great... I present my solution:</p>

<pre><code>
string.replaceAll("(\\.\\.\\.+|[\\p{Po}\\p{Ps}\\p{Pe}\\p{Pi}\\p{Pf}\u2013\u2014\u2015&&[^'\\.]]|(?&lt;!(\\.|\\.\\p{L}))\\.(?=[\\p{Z}\\p{Pf}\\p{Pe}]|\\Z)|(?&lt;!\\p{L})'(?!\\p{L}))"," $1 ")
  .replaceAll("\\p{C}|^\\p{Z}+|\\p{Z}+$","")
  .split("\\p{Z}+")
</code></pre>

<p>Daunting, but I will attempt to explain it... the first line is where most of the magic happens... it is a optional regex group consisting of the following</p>

<ol>
<li><code>\\.\\.\\.+</code> : Captures any ellipses</li>
<li><code>[\\p{Po}\\p{Ps}\\p{Pe}\\p{Pi}\\p{Pf}\u2013\u2014\u2015&&[^'\\.]]</code>: Captures most single punctuation marks. We use mostly 
<a href="http://www.fileformat.info/info/unicode/category/index.htm">unicode categories</a>, in particular all &lsquo;other&rsquo; punctuation, start and end punctuation (brackets, braces, etc.), initial and final quotes, and long dashes. Finally, the group has two unwanted elements &ldquo;.&rdquo; and ', which are removed.</li>
<li><code>(?<!(\\.|\\.\\p{L}))\\.(?=[\\p{Z}\\p{Pf}\\p{Pe}]|\\Z)</code>: This is for full stops, they are kind of hard, as we would like to avoid splitting &ldquo;I.B.M.&rdquo; and of course ellipses. First we use a zero-width look-behind assertion to check that we don't have another full stop or a letter then a full stop. The we look forward and check that the next character is space, an end punctuation, a final quote or the end of the string (that is <code>\\Z</code>)</li>
<li><code>(?<!\\p{L})'(?!\\p{L}))</code>: This finally matches all single quotes, that aren’t  between two letters... ’tis not always correct, but...</li>

<p>The replacement string is then simply whatever matched with a space either side. This generates some extra spaces, of course.</p>

<p>The next pass is quite simple... we remove all initial and trailing spaces, as well as any control characters... it is important to use the Unicode category here as <code>\\s</code> does not match non-breaking space, which occurs quite often in some corpora (e.g., Wikipedia) and allows you to draw triforces, of course.</p>

<p>Finally, we split the text according to the Unicode spaces that are now in the text. This also eliminates all the extra spaces we created in the first step</p>

<p>This tokenization is a little different to some of the more widely known ones, such as the <a href="http://www.cis.upenn.edu/~treebank/tokenization.html">Penn Tree Bank method</a> or Lucene's, however it does not change the original text other than white-space and is very easy-to-use, plus it has no special rules for English and should work well on most languages (with some obvious exception such as Chinese, Japanese and Korean).</p>
</div>
<?php include '../footer.html'; ?>
