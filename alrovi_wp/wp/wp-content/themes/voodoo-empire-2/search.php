<?php get_header(); ?>
  <div id="container" class="clearfix">
   <div id="leftnav">
	  <?php get_sidebar(); ?>
    </div>
    <div id="rightnav">
	  <?php include (TEMPLATEPATH . '/sidebar2.php'); ?>
</div>
    <div id="content">

	<?php if (have_posts()) : ?>

		<h3 class="pagetitle">Search Results</h3>
		
		<div class="navigation">
			<div class="alignleft"><?php next_posts_link('&laquo; Previous Entries') ?></div>
			<div class="alignright"><?php previous_posts_link('Next Entries &raquo;') ?></div>
		</div>


		<?php while (have_posts()) : the_post(); ?>
				
			<div class="post">
				<h3 class="posttitle"><a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title(); ?>"><?php the_title(); ?></a></h3>
				<small><?php the_time('l, F jS, Y') ?></small>
				
				<div class="entry">
					<?php the_excerpt() ?>
				</div>
		
				<p class="postmetadata">Posted in <?php the_category(', ') ?> by: <?php the_author() ?><?php edit_post_link('Edit',' ',''); ?> <br/> <?php comments_popup_link('No Comments', '1 Comment', '% Comments'); ?></p>
			</div>
	
		<?php endwhile; ?>

		<div class="navigation">
			<div class="alignleft"><?php next_posts_link('&laquo; Previous Entries') ?></div>
			<div class="alignright"><?php previous_posts_link('Next Entries &raquo;') ?></div>
		</div>
	
	<?php else : ?>

		<h2 class="center">Not Found</h2>
		<?php include (TEMPLATEPATH . '/searchform.php'); ?>

	<?php endif; ?>
    </div>

    <?php get_footer(); ?>
</div>		
</body>
</html>