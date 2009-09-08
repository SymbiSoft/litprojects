<?php get_header(); ?>

	<div id="content" class="narrowcolumn">
       <div id="twitter_div">
<h2><a href="http://twitter.com/lit_alrovi" id="twitter-link" style="display:block;">alrovi @ Twitter</a></h2>
<ul id="twitter_update_list"></ul>
</div>
<script type="text/javascript" src="http://twitter.com/javascripts/blogger.js"></script>
<script type="text/javascript" src="http://twitter.com/statuses/user_timeline/lit_alrovi.json?callback=twitterCallback2&amp;count=10"></script><a class="twitter" href="http://alrovi.netsons.org/alrovi-twitter/#comments" title="Commenti alrovi@Twitter">Commenti alrovi@Twitter &#187;</a>


</span>
	<?php if (have_posts()) : ?>

		<?php while (have_posts()) : the_post(); ?>

			<div class="post" id="post-<?php the_ID(); ?>">
				<h2><a href="<?php the_permalink() ?>" rel="bookmark" title="Permanent Link to <?php the_title_attribute(); ?>"><?php the_title(); ?></a></h2>
				<small class="date"><?php the_time('F jS, Y') ?> <!-- by <?php the_author() ?> --></small>

				<div class="entry">
					<?php the_content('Continua a leggere &raquo;'); ?>
				</div>

				<p class="postmetadata"><?php the_tags('Tags: ', ', ', '<br />'); ?> Posted in <?php the_category(', ') ?> | <?php edit_post_link('Edit', '', ' | '); ?>  <span class="comment_link"><?php comments_popup_link('No Comments &#187;', '1 Comment &#187;', '% Comments &#187;'); ?></span></p>
			</div>

		<?php endwhile; ?>

		<div class="navigation">
			<div class="alignleft"><?php next_posts_link('&laquo; Older Entries') ?></div>
			<div class="alignright"><?php previous_posts_link('Newer Entries &raquo;') ?></div>
		</div>

	<?php else : ?>

		<h2 class="center">Not Found</h2>
		<p class="center">Sorry, but you are looking for something that isn't here.</p>
		<?php include (TEMPLATEPATH . "/searchform.php"); ?>

	<?php endif; ?>

	</div>

<?php get_sidebar(); ?>

<?php get_footer(); ?>
