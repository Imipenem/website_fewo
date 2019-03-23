            $(document).ready(function(){
                $('#submit').click(function() {
                    if (!$("input[name='datenschutz']:checked").val()) {
                        alert('Bitte willigen sie in unsere Datenschutzerklärung ein');
                        return false;
                    }
                });
             });