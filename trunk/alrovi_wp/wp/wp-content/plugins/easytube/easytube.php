<?php

/*
Plugin Name: Easy Tube
Plugin URI: http://www.ejump.co.uk/wordpress/easytube-plugin-for-wordpress/
Description: Plugin to easliy place YouTube objects in Wordpress Content
Date: 2007, March, 26
Author: Paul Bain
Author URI: http://www.paulbain.co.uk
Version: 1.5
*/

/*
Author: Paul Bain
Website: http://www.paulbain.co.uk
Copyright 2007 Paul Bain All Rights Reserved.


This software is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.

*/



function tube_add_admin()
{
	add_options_page('EasyTube', 'EasyTube', 8, 'easytube', 'tube_options');
}


// 0.8235 = the magic YouTube video ratio! H = (W * 0.8235)
$tube_sizes = array(
						1 =>array(
							"name"	=>"Default - 425 x 355",
							"w"		=>"425",
							"h"		=>"355"
						),
						2 =>array(
							"name"	=>"Large - 700 x 576",
							"w"=>"700",
							"h"=>"576"
						),
						3 =>array(
							"name"	=>"Medium - 350 x 288",
							"w"=>"700",
							"h"=>"576"
						),
						4 =>array(
							"name"	=>"Small - 250 x 206",
							"w"=>"250",
							"h"=>"206"
						)
					);
					
$tube_colors = array(
					1=>array(
						"a"=>"666666",
						"b"=>"d3d3d3"
					),
					2=>array(
						"a"=>"3A3A3A",
						"b"=>"999999"
					),
					3=>array(
						"a"=>"2B405B",
						"b"=>"6B8AB6"
					),
					4=>array(
						"a"=>"006699",
						"b"=>"54ABD6"
					),
					5=>array(
						"a"=>"234900",
						"b"=>"4E9400"
					),
					6=>array(
						"a"=>"E1600F",
						"b"=>"FEBD01"
					),
					7=>array(
						"a"=>"CC2550",
						"b"=>"E87A9F"
					),
					8=>array(
						"a"=>"402061",
						"b"=>"9461CA"
					),
					9=>array(
						"a"=>"5D1719",
						"b"=>"CD311B"
					)
				);


/*
 * The YouTube code 
 */
function tube_content($content) {
	global $tube_sizes, $tube_colors;
	$global = intval(get_option('easytube_global'));
	$size 	= intval(get_option('easytube_size'));
	$border = intval(get_option('easytube_border'));
	$rel	= intval(get_option('easytube_rel'));
	$auto	= intval(get_option('easytube_auto'));
	$color	= intval(get_option('easytube_color'));
	
	
    $regex = '/\[youtube=(.*?)]/i';
	preg_match_all( $regex, $content, $matches );
	for($x=0; $x<count($matches[0]); $x++)
	{
		$parts = explode(" ", $matches[1][$x]);
		$vid= explode('=',$parts[0],2);
		$vid = $vid[1];
		if(is_feed()){
			$replace = "<a href=\"http://www.youtube.com/watch?v=$vid\"><img src=\"http://img.youtube.com/vi/$vid/default.jpg\" width=\"130\" height=\"97\" border=0></a>";
		} else {
			if($global) {
				$replace = '<embed src="http://www.youtube.com/v/'.$vid.'&autoplay='.$auto.'&color1='.$tube_colors[$color]['a'].'&color2='.$tube_colors[$color]['b'].'&rel='.$rel.'&border='.$border.'" type="application/x-shockwave-flash" wmode="transparent" width="'.$tube_sizes[$size]['w'].'" height="'.$tube_sizes[$size]['w'].'"></embed>';
			} else {
				if(count($parts) > 1) {
					$width = $parts[1];
					
					if(count($parts) > 2){
						$height = $parts[2];
					} else {
						$height = ($width * 0.8235);
					}
					$replace = '<object class="embed" width="'.$width.'" height="'.$height.'" type="application/x-shockwave-flash" data="http://www.youtube.com/v/'.$vid.'"><param name="movie" value="http://www.youtube.com/v/'.$vid.'" /><param name="wmode" value="transparent" /><em>You need to a flashplayer enabled browser to view this YouTube video</em></object>';
				} else {
					$vid= explode('=',$matches[1][$x]);
					$vid = $vid[1];
					$replace = '<object class="embed" width="425" height="355" type="application/x-shockwave-flash" data="http://www.youtube.com/v/'.$vid.'"><param name="wmode" value="transparent" /><param name="movie" value="http://www.youtube.com/v/'.$vid.'" /><em>You need to a flashplayer enabled browser to view this YouTube video</em></object>';
				}
			}
		}
		$content = str_replace($matches[0][$x], $replace, $content);
	}
	return $content;
}


/*
 * Google Video Code
 * Settings in options do not work for these... well maybe height will...
 */
function googlevideo_content($content)
{
    $regex = '/\[googlevideo:(.*?)]/i';
	preg_match_all( $regex, $content, $matches );
	for($x=0; $x<count($matches[0]); $x++){
		$parts = explode(" ", $matches[1][$x]);
		if(count($parts) > 1){
			$vid= explode('=',$parts[0]);
			$vid = $vid[1];
			$width = $parts[1];
			
			if(count($parts) > 2){
				$height = $parts[2];
			}
			else {
				$height = "";
			}
			
			$replace = '<object class="embed" width="'.$width.'" height="'.$height.'" type="application/x-shockwave-flash" data="http://video.google.com/googleplayer.swf?docId='.$vid.'"><param name="movie" value="http://video.google.com/googleplayer.swf?docId='.$vid.'" /><em>You need to have flashplayer enabled to watch this Google video</em></object>';
		} else {
			$vid= explode('=',$matches[1][$x]);
			$vid = $vid[1];
			$replace = '<object class="embed" width="425" height="350" type="application/x-shockwave-flash" data="http://video.google.com/googleplayer.swf?docId='.$vid.'"><param name="wmode" value="transparent" /><param name="movie" value="http://video.google.com/googleplayer.swf?docId='.$vid.'" /><em>You need to have flashplayer enabled to watch this Google video</em></object>';
		}
		$content = str_replace($matches[0][$x], $replace, $content);
	}
	return $content;
}

/*
 * The Options page for EasyTube. We rock... thanks.
 */
function tube_options()
{	
	global $tube_sizes,$tube_colors;
	
	$options = array("easytube_global","easytube_border","easytube_rel","easytube_auto");
	
	if($_POST['action'] == 'save')
	{
		update_option('easytube_size', $_POST['easytube_size']);
		update_option('easytube_color', $_POST['easytube_color']);
		foreach($options as $o)
		{	
			
			$val = !empty($_POST[$o]);
			update_option($o, $val);
		}
	}
	
	$global = get_option('easytube_global');
	$size 	= get_option('easytube_size');
	$border = get_option('easytube_border');
	$rel	= get_option('easytube_rel');
	$auto	= get_option('easytube_auto');
	$color	= get_option('easytube_color');
	
	
?>
<!-- EasyTube - its the way forward -->
 <div class="wrap">
	<h2>EasyTube Options</h2>
	
	<?if(!$global){ ?>
	<div style="border: 1px solid red; padding: 5px; ">
	<b style="color: #DF3771">Warning!</b><br />The following options will not take effect if the global checkbox is not checked.
	</div>
	<?} ?>
	
	<form action="?page=easytube" method="POST">
	<input type="hidden" name="action" value="save"/>
	<p class="submit"><input name="Submit" value="Update Options &raquo;" type="submit"></p>
		<table class="optiontable">	
			<tr>
				<th scope="row">
					<b>Enable Global Options</b>
				</th>
				<td>
					<input type="checkbox" name="easytube_global" <?if($global){echo"checked=\"yes\"";}?> value="1" />
				</td>
			</tr>
			<tr>
				<th scope="row">
					Video Dimension
				</th>
				<td>
					<select name="easytube_size">
					<?foreach($tube_sizes as $key=>$s){ ?>
						<option value="<?=$key ?>" <?if($key == $size){ echo "selected=\"selected\"";} ?>><?=$s['name']; ?></option>
					<? } ?>
					</select>
				</td>
			</tr>
			<tr>
				<th scope="row">
					Enable Relevant Videos
				</th>
				<td>
					<input type="checkbox" name="easytube_rel" <?if($rel){echo"checked=\"yes\"";}?> value="1" />
				</td>
			</tr>
			<tr>
				<th scope="row">
					Autoplay Videos
				</th>
				<td>
					<input type="checkbox" name="easytube_auto" <?if($auto){echo"checked=\"yes\"";}?> value="1" />
				</td>
			</tr>
			<tr>
				<th scope="row">
					Enable Embed Border
				</th>
				<td>
					<input type="checkbox" name="easytube_border" <?if($border){echo"checked=\"yes\"";}?> value="1" />
				</td>
			</tr>	
			<tr>
				<th scope="row">
					Border Style:
				</th>
				<td>
					
				</td>
			</tr>		
			<? foreach($tube_colors as $key=>$c){?>
			<tr>
				<th scope="row">
				
				</th>
				<td>
				<INPUT TYPE=RADIO NAME="easytube_color" VALUE="<?=$key ?>" style="float: left;" <?if($color == $key) echo "CHECKED"; ?>><div style="float: left;border: 1px solid #<?=$c['a']; ?>;height: 20px; width: 40px;"><div style="float:left;width: 20px; height: 20px; background-color: #<?=$c['a'] ?>;"></div><div style="float:left;width: 20px; height: 20px; background-color: #<?=$c['b'] ?>;"></div></div>
				</td>
			</tr>
			<?} ?>
		</table>
		<p class="submit"><input name="Submit" value="Update Options &raquo;" type="submit"></p>
	</form>
</div>
<?	
}

/*
 * Install EasyTube options. We like options, they give us variety in life.
 */
function tube_install()
{ 
	add_option('easytube_global', 	0, "Use global settings for easytube");
	add_option('easytube_size', 	1, "Defines video size");
	add_option('easytube_color', 	1, "Defines border color");
	add_option('easytube_border',	0, "Defines if we use a border");
	add_option('easytube_rel',		0, "Show relevant videos");
	add_option('easytube_auto',		0, "Autoplay videos");
}


add_filter('the_content','tube_content');
add_filter('the_content','googlevideo_content');
add_filter('the_excerpt','tube_content');
add_filter('the_excerpt','googlevideo_content');
add_action('admin_menu', 'tube_add_admin');

register_activation_hook(__FILE__,"tube_install");

?>
