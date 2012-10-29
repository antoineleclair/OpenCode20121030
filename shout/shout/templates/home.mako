<!DOCTYPE html>
<html>
<head>
    <title>DemoAF</title>
    <script src="//ajax.googleapis.com/ajax/libs/jquery/1.8.2/jquery.min.js"></script>
</head>
<body>
    <h1>DemoAF</h1>
    <form>
        <p>
            <input type="text" id="text"/>
            <input type="submit"/>
        </p>
    </form>
    <ul id="shout">
        % for broadcast in broadcasts:
            <li>broadcast.content</li>
        % endfor
    </ul>
    
    <script>
        $(function() {
            $('form').submit(function(ev) {
                ev.preventDefault();
            });
        });
    </script>
</body>
</html>
