$(document).ready(function(){
	$('.destroy').on('click', function(e){
		e.preventDefault();
		var id = $(this).data('task');
		$.ajax({
			'url': '/task/'+id,
			'method': 'DELETE',
			'contentType': 'application/json'
		}).success(function(){
			$('#task-'+id).fadeOut('fast', function(){
				$(this).remove();
			});
		})
	});

	$('.toggle').on('click', function(e){
		e.preventDefault();
		var id = $(this).data('task');
		var self = this;
		var checked = $(self).attr('checked');
		$.ajax({
			'url': '/task/'+id,
			'method': 'PUT',
			'contentType': 'application/json',
			'data': JSON.stringify({'complete': !checked})
		}).success(function(data){
			$(self).attr('checked', !checked );
			if (!checked) {
				$('#task-'+id).addClass('completed');
			} else {
				$('#task-'+id).removeClass('completed');
			}
		})
	});
});