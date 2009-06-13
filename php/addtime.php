<?php
    $url="http://www.tvrage.com/myical.php?tid=36422&hash=7195dbe47f229b878028d58cc801cd62";
	$regex="/TZOFFSET(TO|FROM):([+-]\d{4})/";
	$regex2="/TZOFFSEt.*:[+-]\d{4}/";
	$f=fopen($url,"r");
	if ($f) {
		header('Content-type: text/Calendar; charset=utf-8');
		//header('Content-type: text/html; charset=utf-8');
		header("Content-Transfer-Encoding: binary");
		while (!feof($f)) {
			$buffer = fgets($f, 4096);
			if (preg_match($regex, $buffer,$match,PREG_OFFSET_CAPTURE)){
				if ($match[2][0]=="-0400")
					$m="-1000";
				elseif ($match[2][0]=="-0500")
					$m="-1100";
				else $m="succhia";
				$buffer=preg_replace($regex2, $buffer, "TZOFFSET".$match[1][0].":".$m."\n");		
			}
			echo $buffer;
		}
	}
?>
