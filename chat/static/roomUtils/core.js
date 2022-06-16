document.addEventListener('click', function(e){   
  // if (document.getElementById('showlist').contains(e.target)){
  //   document.getElementById("members-list").style.display = 'block';
  // }
  if(document.getElementById('showmore').contains(e.target)){
  	document.getElementById("morelist").style.display='block';
  	document.getElementById("overlay").style.display='block';
  }
  if(document.getElementById('message-area').contains(e.target)){
  	document.getElementById("morelist").style.display='none';
  	// document.getElementById("members-list").style.display = 'none';
  }
  if (document.getElementById("overlay").contains(e.target)) {
  	document.getElementById("morelist").style.display='none';
  	document.getElementById("overlay").style.display='none';
  }
  if (document.getElementById("back").contains(e.target)) {
  	document.getElementById("morelist").style.display='none';
  	document.getElementById("overlay").style.display='none';
  }
});

function scrollToBottom(){
	const messages=document.getElementById("message-area")
	messages.scrollTop = messages.scrollHeight;
}

scrollToBottom()

function formatAMPM(date) {
	var hours = date.getHours();
	var minutes = date.getMinutes();
	var ampm = hours >= 12 ? 'PM' : 'AM';
	hours = hours % 12;
	hours = hours ? hours : 12;
	minutes = minutes < 10 ? '0'+minutes : minutes;
	var strTime = hours + ':' + minutes + ' ' + ampm;
	return strTime;
}

// $('#typing-box').keyup(function (event) {
// 	if (event.keyCode==13){
// 		var content=document.getElementById("typing-box").value;
// 		content=content.replace(/</g, "&lt;").replace(/>/g, "&gt;").trim()
// 		var html='<div class="message-box my-message-box">'+'<div class="message my-message">'+'<div class="user-name"><span>'+formatAMPM(new Date)+'</span> You</div>'+'<p>'+content.toString()+'</p></div>'+'<div class="separator"></div></div>';
// 		if (event.shiftKey){
// 		}else{
// 			document.getElementById("typing-box").value="";
// 			document.getElementById("message-area").innerHTML+=html;
// 			scrollToBottom()
// 		}
// 	}
// })

function hideList(){
	document.getElementById("members-list").style.display = 'none';
}
