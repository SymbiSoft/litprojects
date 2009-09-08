<ul id="sidebarleft">
<?php if ( function_exists('dynamic_sidebar') && dynamic_sidebar(1) ) : else : ?>
<?php get_links_list(); ?>
 <li id="archives"><?php _e('<h2>Archives</h2>'); ?>
 	<ul>
	 <?php wp_get_archives('type=monthly'); ?>
</ul>
 </li>

 <li id="Recent Posts"><?php _e('<h2>Recent Posts</h2>'); ?>
<ul class="menublock">
<p><?php wp_get_archives('type=postbypost&limit=05'); ?></p>			
</ul>
 </li>

 <li id="Recent Comments"><?php _e('<h2>Recent Comments</h2>'); ?>
				<ul>
				<?php include (TEMPLATEPATH . '/simple_recent_comments.php'); ?>
	<?php if (function_exists('src_simple_recent_comments')) { src_simple_recent_comments(5, 40, ''); } ?>
				</ul>
 </li>

 <?php endif; ?>
		</ul>