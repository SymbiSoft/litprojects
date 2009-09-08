<ul id="sidebarright">

<?php if ( function_exists('dynamic_sidebar') && dynamic_sidebar(2) ) : else : ?>

 <li id="pages"><?php _e('<h2>Pages</h2>'); ?>
<ul>
<?php wp_list_pages('sort_column=menu_order&title_li='); ?>
</ul>
 </li>

 <li id="categories"><?php _e('<h2>Categories</h2>'); ?>
	<ul>
	<?php wp_list_cats(''); ?>
	</ul>
 </li>

<?php endif; ?></ul>
