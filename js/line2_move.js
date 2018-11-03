var mouseX, mouseY;  
        var objX, objY;  
        var isDowm = false;  //是否按下鼠标  
        function mouseDown(obj, e) {  
            obj.style.cursor = "move";  
            objX = line_2.style.left;  
            objY = line_2.style.top;  
            mouseX = e.clientX;  
            mouseY = e.clientY;  
            isDowm = true;  
            console.log('按下红线');
        }  
        function mouseMove(e) {  
            //var div =line_2;  
            var x = e.clientX;  
            var y = e.clientY;  
            if (isDowm) {  
                line_2.style.left = parseInt(objX) + parseInt(x) - parseInt(mouseX) + "px";  
                line_2.style.top = parseInt(objY) + parseInt(y) - parseInt(mouseY) + "px";  
                //document.getElementById("span1").innerHTML = "x:" + div.style.top + "  " + "y:" + div.style.left;  
                console.log('按下红线移动'+ "x:" + line_2.style.top + "  " + "y:" + line_2.style.left);
            }
            
        }  
        function mouseUp(e) {  
            if (isDowm) {  
                var x = e.clientX;  
                var y = e.clientY;  
                //var div = document.getElementById("div1");  
                line_2.style.left = (parseInt(x) - parseInt(mouseX) + parseInt(objX)) + "px";  
                line_2.style.top = (parseInt(y) - parseInt(mouseY) + parseInt(objY)) + "px";  
                //document.getElementById("span2").innerHTML = "x:" + div.style.top + "  " + "y:" + div.style.left;  
                mouseX = x;  
                rewmouseY = y;  
                line_2.style.cursor = "default";  
                isDowm = false;  
                
            }  
        }  