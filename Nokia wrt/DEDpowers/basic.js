/*
 * JavaScript file
 */
function init(){
    $("#main").tabs();

	azioni ={
		0: "&loz;",
		1: "&diams;",
		2: "&hearts;",
		3: "&#248;" 
	}
	
	jQuery.each(oggetti,function(){
		$('#oggetti').append("<div class ='oggetto' id=\""+this.nome+"\"><div class ='otitolo'><span class='onome'>"+this.nome+"</span>\n"+
		"<span class = 'azione'>"+azioni[this.azione]+"</span></div>"+
		"<div class='odescrizione'>"+this.descrizione+"</div></div>");
	});
	
	$('div.oggetto').each(function(i){
		var s = $(this);
        var d = $("div.odescrizione", s);
        $("div.otitolo", s).click(function(){
            d.toggle();
        });
	});
	
    var c = 0;
    for (tipo in poteri) {
        var t = "";
        $("#poteri").append("<div id=\"" + tipo + "\"><div class=\"tipo\">" + tipo + "</div>");
        if (tipo != "Volonta") {
            t = "<input type=\"checkbox\">";
        }
        for (var i in poteri[tipo]) {
            p = poteri[tipo][i];
            var az = "<span class=\"azione\">"+azioni[p.azione];
            s = "<div id=potere" + c++ + " class=\"potere\"><div class=\"pheader\">" + t + "<span class=\"pnome\">" + p.nome + "</span>" + az + "</div>\n";
            s += "<div class=\"pdescrizione\">" + p.descrizione + "</div><div/>\n";
            $("div#" + tipo).append(s);
        }
    }
    $("#Volonta div.tipo").html("Volont&agrave;");
    
    $("div.potere").each(function(i){
        var s = $(this);
        var d = $("div.pdescrizione", s);
        $("span.pnome", s).click(function(){
            d.toggle();
        });
    });
    $("div.stato").each(function(i){
        var s = $(this);
        var d = $("div.sdescrizione", s);
        $("div.stitolo", s).click(function(){
            d.toggle();
        });
    });
    $("div.pdescrizione").click(function(){
        $(this).hide();
    });
    
    $("div.potere").each(function(i){
        var s = $(this);
        var id = s.attr("id");
        var d = $("input", s)
        d.change(function(){
            if ($(this).attr("checked")) {
                widget.setPreferenceForKey("t", id);
            }
            else {
                widget.setPreferenceForKey("f", id);
            }
        });
        p = widget.preferenceForKey(id);
        d.attr('checked', p&& p=='t');
    });
	
	$('.iogg').each(function(){
		var c= $(this);
		c.change(function(){
			if (c.attr("checked")) {
                widget.setPreferenceForKey("t", c.attr('id'));
            }
            else {
                widget.setPreferenceForKey("f", c.attr('id'));
            }
		});
		console.log(c.attr('id'))
		var p = widget.preferenceForKey(c.attr('id'));
		c.attr('checked', p&& p=='t');
	})
    
    m = new MenuItem("Reset giornalieri", 0);
    n = new MenuItem("Reset incontro", 1);
    m.onSelect = function(menuId){
        $("input:checked").attr("checked", false).change();
    }
    n.onSelect = function(menuId){
        $("#Incontro input:checked").attr("checked", false).change();
    }
    menu.append(m);
    menu.append(n);
}
