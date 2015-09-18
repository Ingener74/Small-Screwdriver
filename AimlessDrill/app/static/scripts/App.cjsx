React = require 'react'

Title = require './Title.cjsx'

App = React.createClass
    render: ->
        <div>
            <Title />
        </div>

React.render <App />, document.getElementById 'app'