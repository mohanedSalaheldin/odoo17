/** @odoo-module **/

import { registry } from "@web/core/registry";

const { Component, useState } = owl;


export class OwlDevTodoList extends Component{
    setup(){
        this.state = useState({value:1})
    }
}

OwlDevTodoList.template = 'owl_dev.TodoList';
registry.category('actions').add('owl_dev_action_todo_list_js', OwlDevTodoList);