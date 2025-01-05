$(document).ready(function() {
    $('#generateButton').click(function() {
        var jsonInput = $('#jsonInput').val();
        
        try {
            var parsedJson = JSON.parse(jsonInput);
            
            $.ajax({
                type: 'POST',
                url: '/save_json',
                contentType: 'application/json',
                data: JSON.stringify(parsedJson),
                success: function(response) {
                    
                    if (response.success) {
                        console.log('Redirecting to /chat?filename=' + response.filename);
                        window.location.href = '/chat?filename=' + response.filename;
                    } else {
                        alert('Error: ' + response.message);
                    }
                }
            });
        } catch (e) {
            alert('Invalid JSON');
        }
    });
});
