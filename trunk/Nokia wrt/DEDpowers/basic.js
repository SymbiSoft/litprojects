/*
 * JavaScript file
 */
function init(){
	$("#main").tabs();
	
	var c=0;
	for (tipo in poteri) {
		var t="";
		$("#poteri").append("<div id=\"" + tipo + "\"><div class=\"tipo\">" + tipo + "</div>");
		if (tipo!="Volonta"){
			t="<input type=\"checkbox\">";
		} 
		for (var i in poteri[tipo]) {
			p = poteri[tipo][i];
			var az="<span class=\"azione\">";
			switch(p.azione) {
				case MINORE:
					az+="&loz;";
					break;
				case STANDARD:
					az+="&diams;";
					break;
				case GRATUITA:
					az+="&hearts;";
					break;
			}

			s = "<div id=potere" + c++ + " class=\"potere\"><div class=\"pheader\">"+t+"<span class=\"pnome\">" + p.nome + "</span>"+az+"</div>\n";
			s += "<div class=\"pdescrizione\">" + p.descrizione + "</div><div/>\n";
			$("div#" + tipo).append(s);
		}
	}
	$("#Volonta div.tipo").html("Volont&agrave;");
	
	$("div.potere").each(function(i){
		var s=$(this);
		var d=$("div.pdescrizione",s);
		$("span.pnome",s).click(function(){
			d.toggle();
		});
	});
	$("div.stato").each(function(i){
		var s=$(this);
		var d=$("div.sdescrizione",s);
		$("div.stitolo",s).click(function(){
			d.toggle();
		});
	});
	$("div.pdescrizione").click(function(){
		$(this).hide();
	});
	$("#left").click(function(){
		$("#poteri").toggle();
		$("#stati").toggle();
	});
	$("#right").click(function(){
		$("#poteri").toggle();
		$("#stati").toggle();
	});

	$("div.potere").each(function(i){
		var s=$(this);
		var id=s.attr("id");
		var d=$("input",s)
		d.change(function(){
			if ($(this).attr("checked")){
				widget.setPreferenceForKey("t",id);
			}
			else{
				widget.setPreferenceForKey("f",id);
			}
		});
		p=widget.preferenceForKey(id);
		if (p)
			if (p == "t") 
				d.attr('checked', true);
			else
				d.attr('checked', false);
		
	});
		
	m=new MenuItem("Reset giornalieri",0);
	n=new MenuItem("Reset incontro",1);
	m.onSelect=function(menuId){$("input:checked").attr("checked",false).change();}
	n.onSelect=function(menuId){$("#Incontro input:checked").attr("checked",false).change();}
	menu.append(m);
	menu.append(n);
}
