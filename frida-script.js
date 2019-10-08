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

// 
