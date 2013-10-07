$(document).ready(function() 
{	 
	var index = 0;
    var fadeTime = 600;
    var slideTime = 5000;
	var gallery = $("#gallery img");
    var nbImages = gallery.length;
    if (nbImages < 2)
    {
        return;
    }

	for (i = 0; i < nbImages; i++)
	{
		$(gallery[i]).addClass("gallery-image-"+i).hide();
	}
    
    switch_image(nbImages - 1, 0)
    setInterval(slide_show, slideTime);

	function slide_show()
	{
        oldi = index;
 		if (index < (nbImages - 1))
        {   
            index += 1
        }
		else
        {
            index = 0;
        }
        newi = index;
		switch_image(oldi, newi, 600);
	}
    
    function switch_image(oldi, newi, t)
    {   
        $(".gallery-image-" + oldi).fadeOut(t, function () {
            $(".gallery-image-" + newi).fadeIn(t);    
        });
    }
});
