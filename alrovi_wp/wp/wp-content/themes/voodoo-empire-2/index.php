<?php get_header(); ?>

             <div id="container">

	    <div id="leftnav">
              
	  <?php get_sidebar(); ?>
    </div>
    <div id="rightnav">
	  <?php include (TEMPLATEPATH . '/sidebar2.php'); ?>
</div>
    <div id="content">
	
	<?php if (have_posts()) : ?>
		
		<?php while (have_posts()) : the_post(); ?>
				
			<div class="post" id="post-<?php the_ID(); ?>">

<div class="date"> <?php the_time('d') ?>
				<?php the_time('M') ?> </div>
				<h3 class="posttitle"><a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title(); ?>"><?php the_title(); ?></a></h3>

				
				<div class="entry">
					<?php the_content('Continue Reading &raquo;'); ?>
				</div>

	  </div>
			<p class="postmetadata">Filed Under <?php the_category(', ') ?> by: <?php the_author() ?> <br/>Posted with these <?php the_tags(); ?>. <br/><?php edit_post_link('Edit This Entry',' ',''); ?> <br/> <?php comments_popup_link('    No Comments', '    1 Comment', '    % Comments'); ?></p> <br/> 
	
		<?php endwhile; ?>

		<div class="navigation">
			<div class="alignleft"><?php next_posts_link('&laquo; Previous Entries') ?></div>
			<div class="alignright"><?php previous_posts_link('Next Entries &raquo;') ?></div>
		</div>
		
	<?php else : ?>

		<h2 class="center">Not Found</h2>
		<p class="center">Sorry, but you are looking for something that isn't here.</p>
		<?php include (TEMPLATEPATH . "/searchform.php"); ?>

	<?php endif; ?>
    </div>
	

<?php get_footer(); ?>
</div>
</body>
</html>