
		    var Position = {};
		(function () {
		    Position.getAbsolute = function (reference, target) {
		        //因为我们会将目标元素的边框纳入递归公式中，这里先减去对应的值
		        var result = {
		            left: -target.clientLeft,
		            top: -target.clientTop
		        }
		        var node = target;
		        while(node != reference && node != document){
		            result.left = result.left + node.offsetLeft + node.clientLeft;
		            result.top = result.top + node.offsetTop + node.clientTop;
		            node = node.parentNode;
		        }
		        if(isNaN(reference.scrollLeft)){
		            result.right = document.documentElement.scrollWidth - result.left;
		            result.bottom = document.documentElement.scrollHeight - result.top;
		        }else {
		            result.right = reference.scrollWidth - result.left;
		            result.bottom = reference.scrollHeight - result.top;
		        } 
		        return result;
		    }  
		})();
		 
		var result=Position.getAbsolute(document, bar_red); //{left: left, right: right
//	    bar_red.onclick=function(){
//	    	alert(result);
//	    	//console.log(result.bar_red);
//	    }