/** @odoo-module **/

import { registry } from "@web/core/registry";
import { listView } from "@web/views/list/list_view";
import { ListController } from "@web/views/list/list_controller";
import { useService } from "@web/core/utils/hooks";


export class ResPartnerListController extends ListController {
    setup() {
        super.setup();
        this.action = useService("action");
    }

    getSales() {
        console.log("getSales");
        this.action.doAction({
            type: "ir.actions.act_window", 
            name: "Customers Orders",
            res_model: "sale.order",
            views: [[false, 'list'], [false, 'form']],
        });
    }

    getInvoices() {
        console.log("getInvoices");
    }

    getMeetings() {
        console.log("getMeetings");
    }

}

export const resPartnerListController = {
    ...listView,
    Controller: ResPartnerListController,
    buttonTemplate: "owl_dev.web.ListView.Buttons.inherit",
};

registry.category("views").add("res_partner_list_controller", resPartnerListController);