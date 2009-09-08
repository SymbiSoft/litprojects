<?php get_header(); ?>

  <div id="container" class="clearfix">   
	   <div id="leftnav">
	  <?php get_sidebar(); ?>

    </div>
    <div id="rightnav">

	  <?php include (TEMPLATEPATH . '/sidebar2.php'); ?>

</div>
	
    <div id="content">
    <?php if (have_posts()) : while (have_posts()) : the_post(); ?>
		<div class="post" id="post-<?php the_ID(); ?>">
			<h3 class="posttitle"><a href="<?php echo get_permalink() ?>" rel="bookmark" title="Permanent Link: <?php the_title(); ?>"><?php the_title(); ?></a></h3>
			<div class="entrytext">
				<?php the_content('<p class="serif">Read the rest of this page &raquo;</p>'); ?>
	
				<?php link_pages('<p><strong>Pages:</strong> ', '</p>', 'number'); ?>
	
			</div>

		</div>
	  <?php endwhile; endif; ?>
	<?php edit_post_link('Edit this entry.', '<p>', '</p>'); ?>
	<?php comments_template(); ?>
    </div>
	

   <?php get_footer(); ?>	
  </div>
</body>
</html>