<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8" />
<meta NAME="Description" CONTENT="Authors: Stefan Oslowski">
<meta NAME="Keywords" CONTENT="astroph / RFSH, arxiv, Stefan Oslowski">
<title> Astro-PH / Rapid Fire Science Hour</title>
<link rel="stylesheet" href="http://astronomy.swin.edu.au/siteheaders/astro_style.css">
<link rel="stylesheet" href="css/list.css">
<link rel="stylesheet" href="css/page.css">
</head>

<body>
<div id="wrapper">
<header>
<img src="images/swin_logo.png" style="float:left; vertical-align:sub" /><br>
</header>


<?php

$list_code_name_dict = array(
  "astro_most_read" => "ADS: astro: most read",
  "astro_most_cited" => "ADS: astro: most cited",
  "all_most_read" => "ADS: all: most read",
  "all_most_cited" => "ADS: all: most cited",
  "astrobites" => "Recent Astrobites",
  "nature_news" => "Nature News & Comments",
  "phys_org" => "Phys.org featured stories"
);

$list_code_file_dict = array(
  "astro_most_read" => "astro_read",
  "astro_most_cited" => "astro_cited",
  "all_most_read" => "all_read",
  "all_most_cited" => "all_cited",
  "astrobites" => "astrobites",
  "nature_news" => "nature_news",
  "phys_org" => "phys_org_news"
);

$news_list_name_dict = array(
  "nature_news" => "Nature News & Comments",
  "phys_org" => "Phys.org featured stories"
);

$news_list_file_dict = array(
  "nature_news" => "nature_news",
  "phys_org" => "phys_org_news"
);

echo '<br><br><br><br><br><section id="RFHS_suggestions"><div>';
echo '<h3> astroph / RFHS suggestions</h3>';
echo '<p> Please choose a list: '."\n";
echo '<form action="" method="post" class="zielony">'."\n";
echo '<select name="list_type" onchange="this.form.submit()">';
echo '<option value="">Type:</option>'."\n";
foreach ( $list_code_name_dict as $val => $txt )
{
  echo '<option value="'.$val.'">'.$txt.'</option>'."\n";
}
echo '</select></form>'."\n";
echo '</p></div></section>'."\n";

if ($_REQUEST['list_type'])
{
  echo '<section>'."\n";
  echo '<h3> '.$list_code_name_dict[$_REQUEST['list_type']].'</h3>'."\n";
  echo '<div id="list2"><ol>';
  $list_db = new PDO('sqlite:dbs/'.$list_code_file_dict[$_REQUEST['list_type']].'.sqlite');
  $q = 'SELECT * from papers';
  $stmt = $list_db -> query ($q);
  $row_id = 0;
  while ($row = $stmt -> fetch()) {
    $row_id++;
    echo '<li><p><em><a href="'.$row[3].'">'.$row[1].'</a></em>';
    if (strcmp($row[3] , "") !== 0) {
      echo $row[2]."<br>\n";
    }
    if ($row[4] > 0 || $row[5] > 0) {
      echo 'Read '.$row[4]." times<br>Cited ".$row[5].' times';
    }
    echo '</p></li>';
  }
  echo '</ol>';
  echo '</section>';
}

?>
<?php include 'links.php' ?>

<?php include 'footer.php' ?>

</div> <!-- end #wrapper -->
</body>
</html>
