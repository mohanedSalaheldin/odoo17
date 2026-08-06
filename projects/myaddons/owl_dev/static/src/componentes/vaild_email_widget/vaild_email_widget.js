/** @odoo-module **/

import { registry } from "@web/core/registry";
import { EmailField, emailField } from "@web/views/fields/email/email_field";

export class ValidEmailWidget extends EmailField {
    static template = "owl_dev.email.Valid.Widget";

    setup() {
        super.setup();
        console.log("ValidEmailWidget initialized");
    }

    get isValidFormat() {
        const value = this.props.record.data[this.props.name] || "";
        return !value || /\S+@\S+\.\S+/.test(value);
    }
}

export const validEmailWidget = {
    ...emailField,
    component: ValidEmailWidget,
    displayName: "Valid Email",
    supportedTypes: ["char"],
};

registry.category("fields").add("valid_email", validEmailWidget);