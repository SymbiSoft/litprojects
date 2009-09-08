<hr />
<div id="footer">
<!-- If you'd like to support WordPress, having the "powered by" link somewhere on your blog is the best way; it's our only promotion or advertising. -->
	<p>
		<?php bloginfo('name'); ?> is proudly powered by
		<a href="http://wordpress.org/">WordPress</a> and theme designed by <a href="http://www.lavinya.net/">Lavinya</a>
		<br /><span class="enalt"><a href="<?php bloginfo('rss2_url'); ?>">Entries (RSS)</a></span>
		and <span class="enalt"><a href="<?php bloginfo('comments_rss2_url'); ?>">Comments (RSS)</a>.</span>
		 <?php echo get_num_queries(); ?> queries. <?php timer_stop(1); ?> seconds. 
	</p>
</div>
</div>

<?php ?>

		<?php wp_footer(); ?>
<script type="text/javascript">
var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
</script>
<script type="text/javascript">
try {
var pageTracker = _gat._getTracker("UA-180123-4");
pageTracker._trackPageview();
} catch(err) {}</script>
</body>
</html>
