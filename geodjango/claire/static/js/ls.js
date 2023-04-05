
    var url ="{% url 'ld' %}"
    function out_layers(map,options){
        var geoLayer;
        $.getJSON(url, function(json){
         
     
          geoLayer = L.geoJson(json,{
           onEachFeature: function(feature, layer){
            layer.bindTooltip(feature.properties.namelieudit,);
     
           }}).addTo(map)
          
        

        });
  
     
  
  
     }
     