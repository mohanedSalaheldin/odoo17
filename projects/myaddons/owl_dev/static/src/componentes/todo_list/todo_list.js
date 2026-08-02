/** @odoo-module **/

import { registry } from "@web/core/registry";
import { useService } from "@web/core/utils/hooks";
import { Component, useState, onWillStart, useRef } from "@odoo/owl";

export class OwlDevTodoList extends Component {
    setup() {
        this.state = useState({
            task: { name: "", color: "#FF0000", completed: false },
            taskList: [],
            isEdit: false,
            activeId: false,
        });

        this.orm = useService("orm");
        this.model = "owl_dev.todo.list";
        this.searchInput = useRef("search-input");

        onWillStart(async () => {
            await this.getAllTasks();
        });
    }

    async getAllTasks() {
        this.state.taskList = await this.orm.searchRead(
            this.model,
            [],
            ["id", "name", "color", "completed"]
        );
    }

    addTask() {
        this.state.activeId = false;
        this.state.isEdit = false;
        this.clearTask();
    }

    clearTask() {
        this.state.task = {
            name: "",
            color: "#FF0000",
            completed: false,
        };
    }

    editTask(task) {
        this.state.activeId = task.id;
        this.state.isEdit = true;
        this.state.task = { ...task };
    }

    async deleteTask(task) {
        await this.orm.unlink(this.model, [task.id]);
        await this.getAllTasks();
        this.clearTask();
    }

    async saveTask() {
        console.log(this.state.task);
        if (this.state.isEdit) {
            await this.orm.write(this.model, [this.state.activeId], {
                name: this.state.task.name,
                color: this.state.task.color,
                completed: this.state.task.completed,
            });
        } else {
            await this.orm.create(this.model, [
                {
                    name: this.state.task.name,
                    color: this.state.task.color,
                    completed: this.state.task.completed,
                },
            ]);
        }

        await this.getAllTasks();
    }


    async searchTask() {
        const text = this.searchInput.el.value;
        this.state.taskList = await this.orm.searchRead(
            this.model,
            [
                ['name', 'ilike', text],
            ],
            ["id", "name", "color", "completed"]
        );
    }

    async toggleCheck(e, task) {
        const checked = e.target.checked;
        task.completed = checked;
        await this.orm.write(this.model, [task.id], {
            completed: checked,
        });
    }
}

OwlDevTodoList.template = "owl_dev.TodoList";
registry.category("actions").add("owl_dev_action_todo_list_js", OwlDevTodoList);
