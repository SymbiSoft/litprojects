function main(){
	new Request({
			url:"http://localhost:8080/sven.dnd4e",
			method: 'get',
			onSuccess:function(txt,xml){
				/*var d = DOMParser(txt);
				$empty();
				new XML
				
								var d = DOMParser(txt);*/
				parser=new DOMParser();
				xmlDoc=parser.parseFromString(txt,"text/xml");
				$empty();
			}
	}).send();
}
