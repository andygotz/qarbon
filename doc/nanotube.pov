// Persistence of Vision Ray Tracer Scene Description File
// File: ?.pov
// Vers: 3.6
// Desc: Basic Scene Example
// Date: mm/dd/yy
// Auth: ?
//
 
 
 
 
#version 3.6;
 
#include "colors.inc"
 
global_settings {
  assumed_gamma 2.1    
  // used in global_settings, sets an overall brightness/ambient light level in the scene
  ambient_light color rgb <1,1,1>/10
}
 
 
 
 
// ----------------------------------------
 
camera {
  location  <2.4, -0.25, -2.0>     // -0.2  0.0  +0.2    //  -0.3 -0.1 +0.1 +0.3
  direction 1.5*z
  right     x*image_width/image_height
  look_at   <0.0, 0.0,  0.0>
}

/* 
sky_sphere {
  pigment {
    gradient y
    color_map {
      [0.0 rgb <0.6,0.7,1.0>]
      [0.7 rgb <0.0,0.1,0.8>]
    }
  }
}
*/

/*
light_source {
  <-50, 40, -60>            // light's position (translated below)
  color rgb <1, 0, 0>  // light's color
}     
 
light_source {
  <50, 40, -60>            // light's position (translated below)
  color rgb <0, 1, 0>  // light's color
}
 
light_source {
  <0, 190, -60>            // light's position (translated below)
  color rgb <0, 0, 1>  // light's color
 
}
*/

light_source {
  <-50, 40, -60>            // light's position (translated below)
  color rgb <.5, .5, 1>  // light's color
}     
 
light_source {
  <50, 40, -60>            // light's position (translated below)
  color rgb <.5, .5, 1>  // light's color
}

light_source {
  <0, 190, -60>            // light's position (translated below)
  color rgb <.5, .5, 1>  // light's color
}

// ----------------------------------------
 
/*
plane {
  y, -1.3
  pigment { color rgb <0.7,0.5,0.3> }
}
 
*/
 
 
#declare ba=15;
#declare bb=15;
#declare b1=max(ba,bb);
 
#declare s=sqrt(3)/2;

//tube armchair
#declare bb=bb+6;
#declare r=(bb-6)/pi;
#macro ab2y(b,a) sin(a/r)*r  
#end
#macro ab2x(b,a)  b 
#end
#macro ab2z(b,a)  cos(a/r)*r  -r
#end
 

#declare sradius = 0.12;
#declare cradius = sradius / 2;
 
union{
 

#declare m = -b1;
#while (m < b1)
#declare n = -b1;
#while (n < b1)
	#declare a0 = (n*2+m)*s;
    #declare b0 = m*1.5;
 
#if  ((a0<ba) & (a0>-ba) & (b0<bb) & (b0>-bb) )
    union{ 
        #if (b0>-bb+2)
        sphere { <ab2x(a0,b0), ab2y(a0,b0),ab2z(a0,b0)>, sradius }
        #end
        #if ((b0<bb-2) & (b0>-bb+2))
        cylinder { <ab2x(a0,b0), ab2y(a0,b0),ab2z(a0,b0)>,< ab2x(a0,b0+1), ab2y(a0,b0+1),ab2z(a0,b0+1)>, cradius }
        #end
        #if (b0<bb-2)
        sphere {< ab2x(a0,b0+1), ab2y(a0,b0+1),ab2z(a0,b0+1)>, sradius }
 
        #if (a0+s<ba)
        cylinder {< ab2x(a0,b0+1), ab2y(a0,b0+1),ab2z(a0,b0+1)>,< ab2x(a0+s,b0+1.5), ab2y(a0+s,b0+1.5),ab2z(a0+s,b0+1.5)>, cradius }
        #end
        #if (a0-s>-ba)
        cylinder {< ab2x(a0,b0+1), ab2y(a0,b0+1),ab2z(a0,b0+1)>,< ab2x(a0-s,b0+1.5), ab2y(a0-s,b0+1.5),ab2z(a0-s,b0+1.5)>, cradius }
        #end
        #end
    }
#end

#declare n = n+1;   // increment our counter
#end
#declare m = m+1;   // increment our counter
#end
 
 
         texture {
            pigment {
                color rgb <1,1,1>*0.7
            }
            finish{
              specular 0.6
            }
         }
     scale 0.08 //2
     rotate <90,45,0>
     rotate <-20,0,0>
}

