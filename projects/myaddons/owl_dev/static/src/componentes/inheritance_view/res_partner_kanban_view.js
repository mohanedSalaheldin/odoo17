/** @odoo-module **/

import { registry } from "@web/core/registry";
import { kanbanView } from "@web/views/kanban/kanban_view";
import { KanbanController } from "@web/views/kanban/kanban_controller";
import { useService } from "@web/core/utils/hooks";
import { onWillStart } from "@odoo/owl";
export class ResPartnerKanbanController extends KanbanController {
    setup() {
        super.setup();
        this.action = useService("action");
        this.orm = useService("orm");

        onWillStart(async () => {
            this.customerLocations = await this.orm.readGroup("res.partner", [], ['state_id'], ['state_id']);
            console.log(this.customerLocations);
        });
    }

    getSales() {
        console.log("getSales");
        this.action.doAction({
            type: "ir.actions.act_window",
            name: "Customers Orders",
            res_model: "sale.order",
            views: [[false, 'kanban'], [false, 'form']],
        });
    }

    getInvoices() {
        console.log("getInvoices");
    }

    getMeetings() {
        console.log("getMeetings");
    }

    selectLocation(state) {
        const id = state[0];
        const name = state[1];

        this.env.searchModel.createNewFilters([{
            description: name,
            domain:[['state_id', '=', id]],
            isFromAwesomeKanban: true
        }]);
    }
}

ResPartnerKanbanController.template = "owl_dev.web.kanbanView.inherit";

export const resPartnerkanbanController = {
    ...kanbanView,
    Controller: ResPartnerKanbanController,
    buttonTemplate: "owl_dev.web.kanbanView.Buttons.inherit"
};

registry.category("views").add("res_partner_kanban_controller", resPartnerkanbanController);