$(function(){
        //移动窗口的步骤
        //1、按下鼠标左键
        //2、移动鼠标
		line_1.style.marginLeft=0+"px";
        var pagePosition = {
            pX:0,
            pY:0
        };
        var isTouch,eStart,eMove,eEnd,eCancel;
        isTouch = 'ontouchstart' in window;
        eStart = isTouch ? 'touchstart' : 'mousedown',
            eMove = isTouch ? 'touchmove' : 'mousemove',
            eEnd = isTouch ? 'touchend' : 'mouseup',
            eCancel = isTouch ? 'touchcancel' : 'mouseup';

        $(line_1)[0].addEventListener(eStart,function(e){
            getPagePositon(e);
            var positionDiv = $(this).offset();
            var distenceX = pagePosition.pX - positionDiv.left;
            //var distenceY = pagePosition.pY - positionDiv.top;

            $(document)[0].addEventListener(eMove,moveHandler);
            function moveHandler(e){
                //阻止默认的滑动效果
                e.preventDefault();

                getPagePositon(e);
                var x = pagePosition.pX - distenceX;
                //var y = pagePosition.pY - distenceY;
                /*限制在当前document内拖动不出现滚动条*/
                if(x<0){
                    x=0;
                }else if(x>$(document).width()-$(line_1).outerWidth(true)){
                    x = $(document).width()-$(line_1).outerWidth(true);
                }
//                 if(y<0){
//                     y=0;
//                 }else if(y>$(document).height()-$(line_1).outerHeight(true)){
//                     y = $(document).height()-$(line_1).outerHeight(true);
//                 }
                $(line_1).css({
                    'left':x+'px',
                    //'top':y+'px'
                });
				$(line_box).css({
					'left':x+'px',
					//'top':y+'px'
				});
            };
            $(document)[0].addEventListener(eEnd,function(){
                $(document)[0].removeEventListener(eMove,moveHandler);
            });
            /*获取当前页面鼠标x、y*/
            function getPagePositon(e){
                if(!isTouch){
                    pagePosition.pX = e.pageX;
                    //pagePosition.pY = e.pageY;
                }else{
                    pagePosition.pX = e.targetTouches[0].pageX;
                    //pagePosition.pY = e.targetTouches[0].pageY;
                }
            }
        });
    });