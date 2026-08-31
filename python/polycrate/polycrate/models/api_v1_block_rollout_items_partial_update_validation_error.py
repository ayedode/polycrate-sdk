from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_block_rollout_items_partial_update_action_name_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateActionNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_action_run_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateActionRunErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_actual_availability_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_annotations_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_archived_at_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_archived_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_archived_reason_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_block_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateBlockErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_conditions_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateConditionsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_criticality_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_debug_mode_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_discovery_enabled_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_discovery_running_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_discovery_task_id_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_discovery_task_meta_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_display_name_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_kind_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_labels_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_last_state_change_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_last_state_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateLastStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_name_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_non_field_errors_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_platform_service_error_component import (
        ApiV1BlockRolloutItemsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_provider_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_provider_id_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_provider_reference_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_reason_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_reconciliation_enabled_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_reconciliation_running_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_reconciliation_task_id_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_reconciliation_task_meta_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_repair_running_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateRepairRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_repair_task_id_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_repair_task_meta_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_rollout_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateRolloutErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_scope_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_sla_availability_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_sla_target_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_slo_availability_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_slo_target_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_source_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateSourceErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_source_user_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateSourceUserErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_state_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_state_reason_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateStateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_status_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateStatusErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_target_availability_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_partial_update_tolerations_error_component import (
        ApiV1BlockRolloutItemsPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlockRolloutItemsPartialUpdateValidationError")


@_attrs_define
class ApiV1BlockRolloutItemsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlockRolloutItemsPartialUpdateActionNameErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateActionRunErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateActualAvailabilityErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateAnnotationsErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateArchivedAtErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateArchivedErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateArchivedReasonErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateBlockErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateConditionsErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateCriticalityErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateDebugModeErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateDiscoveryRunningErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskIdErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskMetaErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateDisplayNameErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateKindErrorComponent | ApiV1BlockRolloutItemsPartialUpdateLabelsErrorComponent
            | ApiV1BlockRolloutItemsPartialUpdateLastStateChangeErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateLastStateErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateNameErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdatePlatformServiceErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateProviderErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateProviderIdErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateProviderReferenceErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateReasonErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateReconciliationRunningErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskIdErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskMetaErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateRepairRunningErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateRepairTaskIdErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateRepairTaskMetaErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateRolloutErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateScopeErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateSlaTargetErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateSloAvailabilityErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateSloTargetErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateSourceErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateSourceUserErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateStateErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateStateReasonErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateStatusErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1BlockRolloutItemsPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlockRolloutItemsPartialUpdateActionNameErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateActionRunErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateActualAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateAnnotationsErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateArchivedAtErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateArchivedErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateArchivedReasonErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateBlockErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateConditionsErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateCriticalityErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateDebugModeErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateDiscoveryRunningErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskIdErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskMetaErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateDisplayNameErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateKindErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateLabelsErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateLastStateChangeErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateLastStateErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateNameErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdatePlatformServiceErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateProviderErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateProviderIdErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateProviderReferenceErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateReasonErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateReconciliationRunningErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskIdErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskMetaErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateRepairRunningErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateRepairTaskIdErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateRepairTaskMetaErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateRolloutErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateScopeErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateSlaTargetErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateSloTargetErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateSourceErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateSourceUserErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateStateErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateStateReasonErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateStatusErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_block_rollout_items_partial_update_action_name_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateActionNameErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_action_run_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateActionRunErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_actual_availability_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_annotations_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_archived_at_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_archived_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_archived_reason_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_block_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateBlockErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_conditions_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateConditionsErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_criticality_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_debug_mode_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_discovery_enabled_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_discovery_running_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateDiscoveryRunningErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_discovery_task_id_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_discovery_task_meta_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_display_name_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_kind_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_labels_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_last_state_change_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateLastStateChangeErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_last_state_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateLastStateErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_name_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_non_field_errors_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_platform_service_error_component import (
            ApiV1BlockRolloutItemsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_provider_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_provider_id_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_provider_reference_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_reconciliation_running_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateReconciliationRunningErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_repair_running_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateRepairRunningErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_repair_task_id_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateRepairTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_repair_task_meta_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateRepairTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_rollout_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateRolloutErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_scope_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_sla_availability_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_sla_target_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_slo_availability_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_slo_target_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_source_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateSourceErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_source_user_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateSourceUserErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_state_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateStateErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_state_reason_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateStateReasonErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_status_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateStatusErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_target_availability_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_tolerations_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateActionNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateSourceUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateRolloutErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsPartialUpdateActionRunErrorComponent):
                errors_item = errors_item_data.to_dict()
            else:
                errors_item = errors_item_data.to_dict()

            errors.append(errors_item)

        field_dict: dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "type": type_,
                "errors": errors,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: type[T], src_dict: Mapping[str, Any]) -> T:
        from ..models.api_v1_block_rollout_items_partial_update_action_name_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateActionNameErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_action_run_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateActionRunErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_actual_availability_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_annotations_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_archived_at_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_archived_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateArchivedErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_archived_reason_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_block_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateBlockErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_conditions_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateConditionsErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_criticality_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_debug_mode_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateDebugModeErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_discovery_enabled_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_discovery_running_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateDiscoveryRunningErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_discovery_task_id_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_discovery_task_meta_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_display_name_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_kind_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateKindErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_labels_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateLabelsErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_last_state_change_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateLastStateChangeErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_last_state_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateLastStateErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_name_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateNameErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_non_field_errors_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_platform_service_error_component import (
            ApiV1BlockRolloutItemsPartialUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_provider_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateProviderErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_provider_id_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_provider_reference_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_reason_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateReasonErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_reconciliation_running_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateReconciliationRunningErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_repair_running_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateRepairRunningErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_repair_task_id_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateRepairTaskIdErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_repair_task_meta_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateRepairTaskMetaErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_rollout_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateRolloutErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_scope_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateScopeErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_sla_availability_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_sla_target_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateSlaTargetErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_slo_availability_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_slo_target_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateSloTargetErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_source_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateSourceErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_source_user_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateSourceUserErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_state_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateStateErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_state_reason_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateStateReasonErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_status_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateStatusErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_target_availability_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_block_rollout_items_partial_update_tolerations_error_component import (
            ApiV1BlockRolloutItemsPartialUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlockRolloutItemsPartialUpdateActionNameErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateActionRunErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateActualAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateAnnotationsErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateArchivedAtErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateArchivedErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateArchivedReasonErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateBlockErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateConditionsErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateCriticalityErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateDebugModeErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateDiscoveryRunningErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskIdErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskMetaErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateDisplayNameErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateKindErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateLabelsErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateLastStateChangeErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateLastStateErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateNameErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdatePlatformServiceErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateProviderErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateProviderIdErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateProviderReferenceErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateReasonErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateReconciliationRunningErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskIdErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskMetaErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateRepairRunningErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateRepairTaskIdErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateRepairTaskMetaErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateRolloutErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateScopeErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateSlaTargetErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateSloTargetErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateSourceErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateSourceUserErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateStateErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateStateReasonErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateStatusErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_0 = (
                        ApiV1BlockRolloutItemsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_1 = (
                        ApiV1BlockRolloutItemsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_2 = (
                        ApiV1BlockRolloutItemsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_3 = (
                        ApiV1BlockRolloutItemsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_4 = (
                        ApiV1BlockRolloutItemsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_5 = (
                        ApiV1BlockRolloutItemsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_6 = (
                        ApiV1BlockRolloutItemsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_7 = (
                        ApiV1BlockRolloutItemsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_8 = (
                        ApiV1BlockRolloutItemsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_9 = (
                        ApiV1BlockRolloutItemsPartialUpdateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_10 = (
                        ApiV1BlockRolloutItemsPartialUpdateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_11 = (
                        ApiV1BlockRolloutItemsPartialUpdateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_12 = (
                        ApiV1BlockRolloutItemsPartialUpdateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_13 = (
                        ApiV1BlockRolloutItemsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_14 = (
                        ApiV1BlockRolloutItemsPartialUpdateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_15 = (
                        ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_16 = (
                        ApiV1BlockRolloutItemsPartialUpdateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_17 = (
                        ApiV1BlockRolloutItemsPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_18 = (
                        ApiV1BlockRolloutItemsPartialUpdateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_19 = (
                        ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_20 = (
                        ApiV1BlockRolloutItemsPartialUpdateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_21 = (
                        ApiV1BlockRolloutItemsPartialUpdateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_22 = (
                        ApiV1BlockRolloutItemsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_23 = (
                        ApiV1BlockRolloutItemsPartialUpdateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_24 = (
                        ApiV1BlockRolloutItemsPartialUpdateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_25 = (
                        ApiV1BlockRolloutItemsPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_26 = (
                        ApiV1BlockRolloutItemsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_27 = (
                        ApiV1BlockRolloutItemsPartialUpdateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_28 = (
                        ApiV1BlockRolloutItemsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_29 = (
                        ApiV1BlockRolloutItemsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_30 = (
                        ApiV1BlockRolloutItemsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_31 = (
                        ApiV1BlockRolloutItemsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_32 = (
                        ApiV1BlockRolloutItemsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_33 = (
                        ApiV1BlockRolloutItemsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_34 = (
                        ApiV1BlockRolloutItemsPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_35 = (
                        ApiV1BlockRolloutItemsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_36 = (
                        ApiV1BlockRolloutItemsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_37 = (
                        ApiV1BlockRolloutItemsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_38 = (
                        ApiV1BlockRolloutItemsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_39 = (
                        ApiV1BlockRolloutItemsPartialUpdateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_40 = (
                        ApiV1BlockRolloutItemsPartialUpdateActionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_41 = (
                        ApiV1BlockRolloutItemsPartialUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_42 = (
                        ApiV1BlockRolloutItemsPartialUpdateSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_43 = (
                        ApiV1BlockRolloutItemsPartialUpdateSourceUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_44 = (
                        ApiV1BlockRolloutItemsPartialUpdateRolloutErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_partial_update_error_type_45 = (
                        ApiV1BlockRolloutItemsPartialUpdateActionRunErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_block_rollout_items_partial_update_error_type_46 = (
                    ApiV1BlockRolloutItemsPartialUpdateReasonErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_block_rollout_items_partial_update_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_block_rollout_items_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_block_rollout_items_partial_update_validation_error.additional_properties = d
        return api_v1_block_rollout_items_partial_update_validation_error

    @property
    def additional_keys(self) -> list[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
