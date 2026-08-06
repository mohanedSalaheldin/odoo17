/** @odoo-module **/

import { registry } from "@web/core/registry";
import { standardFieldProps } from "@web/views/fields/standard_field_props";
import { Component, useState } from "@odoo/owl";

export class RangeWidget extends Component {
    setup() {
        super.setup();
        this.state = useState({
            range: this.props.record.data[this.props.name] || 0,
        });
        console.log("RangeWidget initialized");
    }

    async onChangeWidget(ev, props) {
        const newSalary = parseInt(ev.target.value);
        await props.record.update({
            [props.name]: newSalary
        });
    }
}

RangeWidget.template = "owl_dev.RangeWidget";
RangeWidget.props = {
    ...standardFieldProps,
};

// Wrap the component in a field definition object
export const rangeWidget = {
    component: RangeWidget,
    displayName: "Range Widget",
    supportedTypes: ["integer", "float"],
};

registry.category("fields").add("range_widget", rangeWidget);