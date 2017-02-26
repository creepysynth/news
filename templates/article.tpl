<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://genshi.edgewall.org/" lang="en">
<head>
  <meta charset="utf-8" />  
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />    
  <link rel="stylesheet" type="text/css" href="/static/style.css" />
  <link rel="icon" type="image/png" href="/static/favicon-64.png" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
  <title>Going to Space</title>
</head>

<body>

<div class="body_inner">
<header>
  <h1>WorldWideNews</h1>
  <a href="/">
    <div class="logo">
      <div class="logo-text">WWN</div>
    </div>
  </a>
</header>

<nav>
  <ul>
    <li><a py:attrs="home" href="/news">Home</a></li>    
    <li><a py:attrs="politics" href="/news/politics">Politics</a></li>
    <li><a py:attrs="business" href="/news/business">Business</a></li>
    <li><a py:attrs="sports" href="/news/sports">Sports</a></li>
    <li><a py:attrs="science" href="/news/science">Science</a></li>
    <li><a py:attrs="entertainment" href="/news/entertainment">Entertainment</a></li>
    <li><a py:attrs="health" href="/news/health">Health</a></li>
    <li class="dropdown">
      <i class="fa fa-bars" ontouchstart=""></i>
      <div class="dropdown-content">
        <a href="/news/politics">Politics</a>
        <a href="/news/business">Business</a>
        <a href="/news/sports">Sports</a>
        <a href="/news/science">Science</a>
        <a href="/news/entertainment">Entertainment</a>
        <a href="/news/health">Health</a>
      </div>
    </li>
  </ul>
</nav>

<article>
  <h1>$header_main</h1>

  <div class="author">$author</div>

  <img src="$main_img" alt="$main_img_alt" />
  <div py:for="paragraph in block_main">
    <p>$paragraph</p>
  </div>
    
  <h2>$block_1_header</h2>
  <div py:for="paragraph in block_1">
    <p>$paragraph</p>
  </div>
  <py:if test="block_1_img">
    <div class="article_img">
      <img src="$block_1_img" alt="$block_1_img_alt" />
    </div>
  </py:if>

  <h2>$block_2_header</h2>
  <div py:for="paragraph in block_2">
    <p>$paragraph</p>
  </div>
  <py:if test="block_2_img">
    <div class="article_img">
      <img src="$block_2_img" alt="$block_2_img_alt" />
    </div>
  </py:if>

  <h2>$block_3_header</h2>
  <div py:for="paragraph in block_3">
    <p>$paragraph</p>
  </div>
  <py:if test="block_3_img">
    <div class="article_img">
      <img src="$block_3_img" alt="$block_3_img_alt" />
    </div>
  </py:if>

  <div class="published">$published</div>
</article>
</div>

</body>
</html>