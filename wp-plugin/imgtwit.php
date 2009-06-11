<?php

/*
Plugin Name: Twitter image from shozu
Plugin URI: http://code.google.com/p/litprojects/source/browse/trunk/wp-plugin/imgtwit.php
Description: Insert images uploaded on shozu in posts posted from Twitter Tools
Date: 2009, june, 10
Author: Carlo Colombo
Author URI: http://code.google.com/p/litprojects/
Version: 0.2
*/

/*
Author: Carlo Colombo
Website: http://code.google.com/p/litprojects/
Copyright 2007 Paul Bain All Rights Reserved.


This software is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

*/



function img_content($content){
	$regex1='$<li><a.*href="(http://tinyurl\.com/[-a-zA-Z0-9]*)".*>$';
	$regex2='$<img src="(http://media\.shozu\.com/cache/portal/media/[a-z0-9]*/[a-z0-9]*_vga)" class="cls" alt="(.*)"/></a>$';	
 
	if (preg_match_all($regex1,$content,$matches, PREG_SET_ORDER)){
		foreach ($matches as $val) {
		    $url=$val[1];
		    $f=fopen($url,"r");
			$buffer="";
		    if ($f) {
				while (!feof($f)) {
				$buffer .= fgets($f, 4096);
	  			}
	      		fclose($f);
				if (preg_match_all($regex2,$buffer,$match,PREG_SET_ORDER)){
					$img=$match[0];
					$imgtag='<img src="'.$img[1].'" alt="'.$img[2].'" height="150"/>';
					$atag='<a href="'.$url.'" title="'.$img[2].'">'.$imgtag."</a><br/>\n";
	      			$regex_replace='$<a.*"'.$url.'".*>'.$url.'</a>$';
					$content=preg_replace($regex_replace,$atag,$content);
				}
			}
		}
	}
	return $content;
}

add_filter('the_content','img_content');
?>

