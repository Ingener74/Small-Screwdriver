React = require 'react'

App = React.createClass
    render: ->
        <div>
            <p>Aimless Drill</p>
        </div>

React.render <App />, document.getElementById 'app'