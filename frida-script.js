// webview loadurl("java.lang.String","java.Util.Map")
Java.perform(function(){
  var Webview = Java.use("android.webkit.WebView");
  Webview.loadUrl.overload("java.lang.String","java.Util.Map").implementation = function(url,data){
    console.log("\n[+]Loading URL from: ",url);
    console.log("\n[+]Setting the value of setWebContentsDebuggingEnable() to True");
    this.setWebContentsDebuggingEnabled(true);
    var HashMapNode = Java.use("java.util.HashMap$Node");
    var iterator = data.entrySet().iterator();
    while (iterator.hasNext()){
      var entry = java.cast(iterator.next(),HashMapNode);
      console.log("\n[+]Key: ",entry.getKey());
      console.log("\n[+]Value: ",entry.getValue());
    }
    this.loadUrl.overload("java.lang.String","java.Util.Map").call(this,url,data);
  }
})



// enum loaded classes
Java.perform(function(){
  Java.enumerateLoadedClasses({
    "onMatch":function(className){ 
      console.log(className)
    },
    "onComplete":function(){
      console.log("Done !!!")
    }
  })
})

// filter instances
Java.choose("asvid.github.io.fridaapp.MainActivity" , {
  onMatch : function(instance){ 
    console.log("Found instance: "+instance);
    instance.showToast();
  },
  onComplete:function(){}
});

// filter class by name
Java.enumerateLoadedClasses( {
  "onMatch": function(className){
        if(className.includes("asvid")){
            console.log(className);
        }            
    },
  "onComplete":function(){}
  }
);




