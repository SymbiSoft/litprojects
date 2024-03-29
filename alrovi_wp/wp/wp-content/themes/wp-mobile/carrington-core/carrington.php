<?php

// This file is part of the Carrington Theme Framework for WordPress
// http://carringtontheme.com
//
// Copyright (c) 2008-2009 Crowd Favorite, Ltd. All rights reserved.
// http://crowdfavorite.com
//
// Released under the GPL license
// http://www.opensource.org/licenses/gpl-license.php
//
// **********************************************************************
// This program is distributed in the hope that it will be useful, but
// WITHOUT ANY WARRANTY; without even the implied warranty of
// MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. 
// **********************************************************************

if (__FILE__ == $_SERVER['SCRIPT_FILENAME']) { die(); }

//	ini_set('display_errors', '1');
//	ini_set('error_reporting', E_ALL);

load_theme_textdomain('carrington');

$cfct_options[] = 'cfct_about_text';
$cfct_options[] = 'cfct_credit';
$cfct_options[] = 'cfct_wp_footer';

include_once(CFCT_PATH.'carrington-core/admin.php');
include_once(CFCT_PATH.'carrington-core/templates.php');
include_once(CFCT_PATH.'carrington-core/utility.php');
include_once(CFCT_PATH.'carrington-core/ajax-load.php');
include_once(CFCT_PATH.'carrington-core/attachment.php');
include_once(CFCT_PATH.'carrington-core/compatibility.php');

cfct_load_plugins();

function cfct_init() {
	cfct_admin_request_handler();
	if (cfct_get_option('cfct_ajax_load') == 'yes') {
		cfct_ajax_load();
	}
}
add_action('init', 'cfct_init');

function cfct_wp_footer() {
	echo get_option('cfct_wp_footer');
}
add_action('wp_footer', 'cfct_wp_footer');

function cfct_about_text() {
	$about_text = get_option('cfct_about_text');
	if (!empty($about_text)) {
		$about_text = wptexturize($about_text);
		$about_text = convert_smilies($about_text);
		$about_text = convert_chars($about_text);
		$about_text = wpautop($about_text);
	}
	else {
		global $post;
		remove_filter('the_excerpt', 'st_add_widget');
		$about_query = new WP_Query('pagename=about');
		while ($about_query->have_posts()) {
			$about_query->the_post();
			$about_text = get_the_excerpt().sprintf(__('<a class="more" href="%s">more &rarr;</a>', 'carrington'), get_permalink());
		}
	}
	if (function_exists('st_add_widget')) {
		add_filter('the_excerpt', 'st_add_widget');
	}
	return $about_text;
}

if (!defined('CFCT_DEBUG')) {
	define('CFCT_DEBUG', false);
}

?>