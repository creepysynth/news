<html xmlns="http://www.w3.org/1999/xhtml" xmlns:py="http://genshi.edgewall.org/" lang="en">
<head>
  <meta charset="utf-8" />  
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />    
  <link rel="stylesheet" type="text/css" href="/static/style.css" />
  <link rel="icon" type="image/png" href="/static/favicon-64.png" />
  <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css" />
  <title>$title</title>
</head>

<body>

<div class="body_inner">
<header>
  <h1>WorldWideNews</h1>
  <a href="/news">
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

<div class="subcategory">Most popular</div>

<div class="row">
  <a class="block-reference" href="$main_href">
    <div class="col-8 col-m-8 main">
      <div id="container">
        <img src="$main_img" alt="$main_alt" />
          <div class="desc">$main_header</div>
          <p>$main_text</p>
      </div>
    </div>
  </a>

  <a class="block-reference" href="$side1_href">
    <div class="col-4 col-m-4 column">
      <img src="$side1_img" alt="$side1_alt" />
      <div class="desc">$side1_desc</div>
    </div>
  </a>

  <a class="block-reference" href="$side2_href">
    <div class="col-4 col-m-4 column">
      <img src="$side2_img" alt="$side2_alt" />
      <div class="desc">$side2_desc</div>
    </div>
  </a>
</div>

<div class="subcategory">Latest</div>

<div class="row">
  <a class="block-reference" href="$col1_href">
    <div class="col-4 col-m-4 column">
      <img src="$col1_img" alt="$col1_alt" />
      <div class="desc">$col1_desc</div>
    </div>
  </a>

  <a class="block-reference" href="$col2_href">
    <div class="col-4 col-m-4 column">
      <img src="$col2_img" alt="$col2_alt" />
      <div class="desc">$col2_desc</div>
    </div>
  </a>

  <a class="block-reference" href="$col3_href">
    <div class="col-4 col-m-4 column">
      <img src="$col3_img" alt="$col3_alt" />
      <div class="desc">$col3_desc</div>
    </div>
  </a>

  <a class="block-reference" href="$col4_href">
    <div class="col-4 col-m-4 column">
      <img src="$col4_img" alt="$col4_alt" />
      <div class="desc">$col4_desc</div>
    </div>
  </a>

  <a class="block-reference" href="$col5_href">
    <div class="col-4 col-m-4 column">
      <img src="$col5_img" alt="$col5_alt" />
      <div class="desc">$col5_desc</div>
    </div>
  </a>

  <a class="block-reference" href="$col6_href">
    <div class="col-4 col-m-4 column">
      <img src="$col6_img" alt="$col6_alt" />
      <div class="desc">$col6_desc</div>
    </div>
  </a>
</div>

<footer>Copyright &copy; 2016 WWN</footer>
</div>

</body>
</html>