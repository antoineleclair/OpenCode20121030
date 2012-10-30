<!DOCTYPE html>
<html>
<head>
    <title>DemoAF</title>
</head>
<body>
    <h1>DemoAF</h1>
    <form method="post" action="${request.route_url('shout')}">
        <p>
            <input type="text" name="content"/>
            <input type="submit"/>
        </p>
    </form>
    <ul id="shout">
        % for broadcast in broadcasts:
            <li id="shout_${broadcast.id}">${broadcast.content}</li>
        % endfor
    </ul>    
</body>
</html>
