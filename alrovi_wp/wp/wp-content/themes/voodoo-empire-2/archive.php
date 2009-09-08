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

		 <?php $post = $posts[0]; // Hack. Set $post so that the_date() works. ?>
<?php /* If this is a category archive */ if (is_category()) { ?>				
		<h4 class="pagetitle">Archive for the '<?php echo single_cat_title(); ?>' Category</h4>
		
 	  <?php /* If this is a daily archive */ } elseif (is_day()) { ?>
		<h4 class="pagetitle">Archive for <?php the_time('F jS, Y'); ?></h4>
		
	 <?php /* If this is a monthly archive */ } elseif (is_month()) { ?>
		<h4 class="pagetitle">Archive for <?php the_time('F, Y'); ?></h4>

		<?php /* If this is a yearly archive */ } elseif (is_year()) { ?>
		<h4 class="pagetitle">Archive for <?php the_time('Y'); ?></h4>
		
	  <?php /* If this is a search */ } elseif (is_search()) { ?>
		<h4 class="pagetitle">Search Results</h4>
		
	  <?php /* If this is an author archive */ } elseif (is_author()) { ?>
		<h4 class="pagetitle">Author Archive</h4>

		<?php /* If this is a paged archive */ } elseif (isset($_GET['paged']) && !empty($_GET['paged'])) { ?>
		<h4 class="pagetitle">Blog Archives</h4>

		<?php } ?>


		<div class="navigation">
			<div class="alignleft"><?php next_posts_link('&laquo; Previous Entries') ?></div>
			<div class="alignright"><?php previous_posts_link('Next Entries &raquo;') ?></div>
		</div>

		<?php while (have_posts()) : the_post(); ?>
		<div class="post" id="post-<?php the_ID(); ?>">

<div class="date"> <?php the_time('d') ?>
				<?php the_time('M') ?> </div>
				<h3 class="posttitle"><a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title(); ?>"><?php the_title(); ?></a></h3>
				
				<div class="entry">
					<?php the_content() ?>
				</div>
		
				<p class="postmetadata">Posted in <?php the_category(', ') ?> by: <?php the_author() ?><br/>With with these <?php the_tags(); ?>.<?php edit_post_link('Edit',' ',''); ?> <br/> <?php comments_popup_link('No Comments', '1 Comment', '% Comments'); ?></p> 

			</div>
	
		<?php endwhile; ?>

		<div class="navigation">
			<div class="alignleft"><?php next_posts_link('&laquo; Previous Entries') ?></div>
			<div class="alignright"><?php previous_posts_link('Next Entries &raquo;') ?></div>
		</div>
	
	<?php else : ?>

		<h4 class="center">Not Found</h4>
		<?php include (TEMPLATEPATH . '/searchform.php'); ?>

	<?php endif; ?>
    </div>

    <?php get_footer(); ?>
</div>
</body>
</html>