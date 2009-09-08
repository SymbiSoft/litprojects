<?php
/**
 * Retrieves and creates the wp-config.php file.
 *
 * The permissions for the base directory must allow for writing files in order
 * for the wp-config.php to be created using this page.
 *
 * @package WordPress
 * @subpackage Administration
 */

/**
 * We are installing.
 *
 * @package WordPress
 */
define('WP_INSTALLING', true);

/**#@+
 * These three defines are required to allow us to use require_wp_db() to load
 * the database class while being wp-content/db.php aware.
 * @ignore
 */
define('ABSPATH', dirname(dirname(__FILE__)).'/');
define('WPINC', 'wp-includes');
define('WP_CONTENT_DIR', ABSPATH . 'wp-content');
/**#@-*/

require_once('../wp-includes/compat.php');
require_once('../wp-includes/functions.php');
require_once('../wp-includes/classes.php');

if (!file_exists('../wp-config-sample.php'))
	wp_die('Spiacente, mi serve un file wp-config-sample.php su cui lavorare. Per favore ricaricare questo file dalla installazione di WordPress.');

$configFile = file('../wp-config-sample.php');

if ( !is_writable('../'))
	wp_die("Spiacente, non posso scrivere la directory. Occorre cambiare i permessi sulla directory di WordPress o creare il file wp-config.php manualmente.");

// Check if wp-config.php has been created
if (file_exists('../wp-config.php'))
	wp_die("<p>The file 'wp-config.php' already exists. If you need to reset any of the configuration items in this file, please delete it first. You may try <a href='install.php'>installing now</a>.</p>");

// Check if wp-config.php exists above the root directory
if (file_exists('../../wp-config.php') && ! file_exists('../../wp-load.php'))
	wp_die("<p>Il file 'wp-config.php' esiste già ad un livello superiore rispetto a quello dell'installazione di WordPress. Se si desidera azzerare uno qualsiasi degli elementi di configurazione di questo file, cancellarlo. &Egrave; anche possibile <a href='install.php'>provare ad installare ora</a>.</p>");

if (isset($_GET['step']))
	$step = $_GET['step'];
else
	$step = 0;

/**
 * Display setup wp-config.php file header.
 *
 * @ignore
 * @since 2.3.0
 * @package WordPress
 * @subpackage Installer_WP_Config
 */
function display_header() {
	header( 'Content-Type: text/html; charset=utf-8' );
?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
<title>WordPress &rsaquo; Impostazione File di Configurazione</title>
<link rel="stylesheet" href="css/install.css" type="text/css" />

</head>
<body>
<h1 id="logo"><img alt="WordPress" src="images/wordpress-logo.png" /></h1>
<?php
}//end function display_header();

switch($step) {
	case 0:
		display_header();
?>

<p>Benvenuti in WordPress. Prima di iniziare ci occorrono alcune informazioni sul database. Occorre conoscere i seguenti elementi prima di procedere.</p>
<ol>
	<li>Nome del database</li>
	<li>Username del database</li>
	<li>Password del database</li>
	<li>Host del database</li>
	<li>Prefisso tabella (se si desidera eseguire diverse istanze di WordPress con un solo database) </li>
</ol>
<p><strong>Se per qualsiasi ragione la creazione automatica del file non funzionasse non preoccuparsi. Tutto quello che si deve fare &egrave; immettere le informazioni sul database in un file di configurazione. &Egrave;possibile anche semplicemente aprire il file <code>wp-config-sample.php</code> con un editor di testo, immettere le informazioni e salvare il file come <code>wp-config.php</code>. </strong></p>
<p>In ogni caso, queste informazioni vengono fornite dal proprio ISP. Se non si dispone di tali informazioni, allora si dovr&agrave; contattarlo prima di proseguire. Se si &egrave; pronti <a href="setup-config.php?step=1">iniziamo</a>! </p>

<p class="step"><a href="setup-config.php?step=1" class="button">Partiamo!</a></p>
<?php
	break;

	case 1:
		display_header();
	?>
<form method="post" action="setup-config.php?step=2">
	<p>Di seguito si dovranno immettere i dettagli della connessione al database. Se non si &egrave; sicuri riguardo a questi dati, contattare il proprio fornitore di hosting.</p>
	<table class="form-table">
		<tr>
			<th scope="row"><label for="dbname">Nome del database</label></th>
			<td><input name="dbname" id="dbname" type="text" size="25" value="wordpress" /></td>
			<td>Il nome del database da usare per far funzionare WP. </td>
		</tr>
		<tr>
			<th scope="row"><label for="uname">Nome utente</label></th></th>
			<td><input name="uname" id="uname" type="text" size="25" value="username" /></td>
			<td>Il nome utente MySQL</td>
		</tr>
		<tr>
			<th scope="row"><label for="pwd">Password</label></th>
			<td><input name="pwd" id="pwd" type="text" size="25" value="password" /></td>
			<td>...e la password MySQL.</td>
		</tr>
		<tr>
			<th scope="row"><label for="dbhost">Host del database</label></th>
			<td><input name="dbhost" id="dbhost" type="text" size="25" value="localhost" /></td>
			<td>al 99% non si dovr&agrave; cambiare questa impostazione.</td>
		</tr>
		<tr>
			<th scope="row"><label for="prefix">Prefisso tabella</label></th>
			<td><input name="prefix" id="prefix" type="text" id="prefix" value="wp_" size="25" /></td>
			<td>Se si desidera eseguire pi&ugrave; istanze di WordPress con un singolo database, modificare questo valore.</td>
		</tr>
	</table>
	<p class="step"><input name="submit" type="submit" value="Prosegui" class="button" /></p>
</form>
<?php
	break;

	case 2:
	$dbname  = trim($_POST['dbname']);
	$uname   = trim($_POST['uname']);
	$passwrd = trim($_POST['pwd']);
	$dbhost  = trim($_POST['dbhost']);
	$prefix  = trim($_POST['prefix']);
	if (empty($prefix)) $prefix = 'wp_';

	// Test the db connection.
	/**#@+
	 * @ignore
	 */
	define('DB_NAME', $dbname);
	define('DB_USER', $uname);
	define('DB_PASSWORD', $passwrd);
	define('DB_HOST', $dbhost);
	/**#@-*/

	// We'll fail here if the values are no good.
	require_wp_db();
	if ( !empty($wpdb->error) )
		wp_die($wpdb->error->get_error_message());

	$handle = fopen('../wp-config.php', 'w');

	foreach ($configFile as $line_num => $line) {
		switch (substr($line,0,16)) {
			case "define('DB_NAME'":
				fwrite($handle, str_replace("putyourdbnamehere", $dbname, $line));
				break;
			case "define('DB_USER'":
				fwrite($handle, str_replace("'usernamehere'", "'$uname'", $line));
				break;
			case "define('DB_PASSW":
				fwrite($handle, str_replace("'yourpasswordhere'", "'$passwrd'", $line));
				break;
			case "define('DB_HOST'":
				fwrite($handle, str_replace("localhost", $dbhost, $line));
				break;
			case '$table_prefix  =':
				fwrite($handle, str_replace('wp_', $prefix, $line));
				break;
			default:
				fwrite($handle, $line);
		}
	}
	fclose($handle);
	chmod('../wp-config.php', 0666);

	display_header();
?>
<p>Tutto a posto! Si &egrave; superata questa fase della installazione. Ora WordPress pu&ograve; comunicare con il database. Se si &egrave, pronti ora &egrave; il momento di <a href="install.php">eseguire la installazione!</a></p>

<p class="step"><a href="install.php" class="button">Avvia installazione</a></p>
<?php
	break;
}
?>
</body>
</html>
