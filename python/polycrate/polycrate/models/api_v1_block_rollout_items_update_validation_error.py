from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_block_rollout_items_update_action_name_error_component import (
        ApiV1BlockRolloutItemsUpdateActionNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_action_run_error_component import (
        ApiV1BlockRolloutItemsUpdateActionRunErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_actual_availability_error_component import (
        ApiV1BlockRolloutItemsUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_annotations_error_component import (
        ApiV1BlockRolloutItemsUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_archived_at_error_component import (
        ApiV1BlockRolloutItemsUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_archived_error_component import (
        ApiV1BlockRolloutItemsUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_archived_reason_error_component import (
        ApiV1BlockRolloutItemsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_block_error_component import (
        ApiV1BlockRolloutItemsUpdateBlockErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_conditions_error_component import (
        ApiV1BlockRolloutItemsUpdateConditionsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_criticality_error_component import (
        ApiV1BlockRolloutItemsUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_debug_mode_error_component import (
        ApiV1BlockRolloutItemsUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_discovery_enabled_error_component import (
        ApiV1BlockRolloutItemsUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_discovery_running_error_component import (
        ApiV1BlockRolloutItemsUpdateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_discovery_task_id_error_component import (
        ApiV1BlockRolloutItemsUpdateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_discovery_task_meta_error_component import (
        ApiV1BlockRolloutItemsUpdateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_display_name_error_component import (
        ApiV1BlockRolloutItemsUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_kind_error_component import (
        ApiV1BlockRolloutItemsUpdateKindErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_labels_error_component import (
        ApiV1BlockRolloutItemsUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_last_state_change_error_component import (
        ApiV1BlockRolloutItemsUpdateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_last_state_error_component import (
        ApiV1BlockRolloutItemsUpdateLastStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_name_error_component import (
        ApiV1BlockRolloutItemsUpdateNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_non_field_errors_error_component import (
        ApiV1BlockRolloutItemsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_platform_service_error_component import (
        ApiV1BlockRolloutItemsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_provider_error_component import (
        ApiV1BlockRolloutItemsUpdateProviderErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_provider_id_error_component import (
        ApiV1BlockRolloutItemsUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_provider_reference_error_component import (
        ApiV1BlockRolloutItemsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_reason_error_component import (
        ApiV1BlockRolloutItemsUpdateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_reconciliation_enabled_error_component import (
        ApiV1BlockRolloutItemsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_reconciliation_running_error_component import (
        ApiV1BlockRolloutItemsUpdateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_reconciliation_task_id_error_component import (
        ApiV1BlockRolloutItemsUpdateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_reconciliation_task_meta_error_component import (
        ApiV1BlockRolloutItemsUpdateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_repair_running_error_component import (
        ApiV1BlockRolloutItemsUpdateRepairRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_repair_task_id_error_component import (
        ApiV1BlockRolloutItemsUpdateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_repair_task_meta_error_component import (
        ApiV1BlockRolloutItemsUpdateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_rollout_error_component import (
        ApiV1BlockRolloutItemsUpdateRolloutErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_scope_error_component import (
        ApiV1BlockRolloutItemsUpdateScopeErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_sla_availability_error_component import (
        ApiV1BlockRolloutItemsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_sla_target_error_component import (
        ApiV1BlockRolloutItemsUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_slo_availability_error_component import (
        ApiV1BlockRolloutItemsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_slo_target_error_component import (
        ApiV1BlockRolloutItemsUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_source_error_component import (
        ApiV1BlockRolloutItemsUpdateSourceErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_source_user_error_component import (
        ApiV1BlockRolloutItemsUpdateSourceUserErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_state_error_component import (
        ApiV1BlockRolloutItemsUpdateStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_state_reason_error_component import (
        ApiV1BlockRolloutItemsUpdateStateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_status_error_component import (
        ApiV1BlockRolloutItemsUpdateStatusErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_target_availability_error_component import (
        ApiV1BlockRolloutItemsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_update_tolerations_error_component import (
        ApiV1BlockRolloutItemsUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlockRolloutItemsUpdateValidationError")


@_attrs_define
class ApiV1BlockRolloutItemsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlockRolloutItemsUpdateActionNameErrorComponent |
            ApiV1BlockRolloutItemsUpdateActionRunErrorComponent |
            ApiV1BlockRolloutItemsUpdateActualAvailabilityErrorComponent |
            ApiV1BlockRolloutItemsUpdateAnnotationsErrorComponent | ApiV1BlockRolloutItemsUpdateArchivedAtErrorComponent |
            ApiV1BlockRolloutItemsUpdateArchivedErrorComponent | ApiV1BlockRolloutItemsUpdateArchivedReasonErrorComponent |
            ApiV1BlockRolloutItemsUpdateBlockErrorComponent | ApiV1BlockRolloutItemsUpdateConditionsErrorComponent |
            ApiV1BlockRolloutItemsUpdateCriticalityErrorComponent | ApiV1BlockRolloutItemsUpdateDebugModeErrorComponent |
            ApiV1BlockRolloutItemsUpdateDiscoveryEnabledErrorComponent |
            ApiV1BlockRolloutItemsUpdateDiscoveryRunningErrorComponent |
            ApiV1BlockRolloutItemsUpdateDiscoveryTaskIdErrorComponent |
            ApiV1BlockRolloutItemsUpdateDiscoveryTaskMetaErrorComponent |
            ApiV1BlockRolloutItemsUpdateDisplayNameErrorComponent | ApiV1BlockRolloutItemsUpdateKindErrorComponent |
            ApiV1BlockRolloutItemsUpdateLabelsErrorComponent | ApiV1BlockRolloutItemsUpdateLastStateChangeErrorComponent |
            ApiV1BlockRolloutItemsUpdateLastStateErrorComponent | ApiV1BlockRolloutItemsUpdateNameErrorComponent |
            ApiV1BlockRolloutItemsUpdateNonFieldErrorsErrorComponent |
            ApiV1BlockRolloutItemsUpdatePlatformServiceErrorComponent | ApiV1BlockRolloutItemsUpdateProviderErrorComponent |
            ApiV1BlockRolloutItemsUpdateProviderIdErrorComponent |
            ApiV1BlockRolloutItemsUpdateProviderReferenceErrorComponent | ApiV1BlockRolloutItemsUpdateReasonErrorComponent |
            ApiV1BlockRolloutItemsUpdateReconciliationEnabledErrorComponent |
            ApiV1BlockRolloutItemsUpdateReconciliationRunningErrorComponent |
            ApiV1BlockRolloutItemsUpdateReconciliationTaskIdErrorComponent |
            ApiV1BlockRolloutItemsUpdateReconciliationTaskMetaErrorComponent |
            ApiV1BlockRolloutItemsUpdateRepairRunningErrorComponent | ApiV1BlockRolloutItemsUpdateRepairTaskIdErrorComponent
            | ApiV1BlockRolloutItemsUpdateRepairTaskMetaErrorComponent | ApiV1BlockRolloutItemsUpdateRolloutErrorComponent |
            ApiV1BlockRolloutItemsUpdateScopeErrorComponent | ApiV1BlockRolloutItemsUpdateSlaAvailabilityErrorComponent |
            ApiV1BlockRolloutItemsUpdateSlaTargetErrorComponent | ApiV1BlockRolloutItemsUpdateSloAvailabilityErrorComponent
            | ApiV1BlockRolloutItemsUpdateSloTargetErrorComponent | ApiV1BlockRolloutItemsUpdateSourceErrorComponent |
            ApiV1BlockRolloutItemsUpdateSourceUserErrorComponent | ApiV1BlockRolloutItemsUpdateStateErrorComponent |
            ApiV1BlockRolloutItemsUpdateStateReasonErrorComponent | ApiV1BlockRolloutItemsUpdateStatusErrorComponent |
            ApiV1BlockRolloutItemsUpdateTargetAvailabilityErrorComponent |
            ApiV1BlockRolloutItemsUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlockRolloutItemsUpdateActionNameErrorComponent
        | ApiV1BlockRolloutItemsUpdateActionRunErrorComponent
        | ApiV1BlockRolloutItemsUpdateActualAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsUpdateAnnotationsErrorComponent
        | ApiV1BlockRolloutItemsUpdateArchivedAtErrorComponent
        | ApiV1BlockRolloutItemsUpdateArchivedErrorComponent
        | ApiV1BlockRolloutItemsUpdateArchivedReasonErrorComponent
        | ApiV1BlockRolloutItemsUpdateBlockErrorComponent
        | ApiV1BlockRolloutItemsUpdateConditionsErrorComponent
        | ApiV1BlockRolloutItemsUpdateCriticalityErrorComponent
        | ApiV1BlockRolloutItemsUpdateDebugModeErrorComponent
        | ApiV1BlockRolloutItemsUpdateDiscoveryEnabledErrorComponent
        | ApiV1BlockRolloutItemsUpdateDiscoveryRunningErrorComponent
        | ApiV1BlockRolloutItemsUpdateDiscoveryTaskIdErrorComponent
        | ApiV1BlockRolloutItemsUpdateDiscoveryTaskMetaErrorComponent
        | ApiV1BlockRolloutItemsUpdateDisplayNameErrorComponent
        | ApiV1BlockRolloutItemsUpdateKindErrorComponent
        | ApiV1BlockRolloutItemsUpdateLabelsErrorComponent
        | ApiV1BlockRolloutItemsUpdateLastStateChangeErrorComponent
        | ApiV1BlockRolloutItemsUpdateLastStateErrorComponent
        | ApiV1BlockRolloutItemsUpdateNameErrorComponent
        | ApiV1BlockRolloutItemsUpdateNonFieldErrorsErrorComponent
        | ApiV1BlockRolloutItemsUpdatePlatformServiceErrorComponent
        | ApiV1BlockRolloutItemsUpdateProviderErrorComponent
        | ApiV1BlockRolloutItemsUpdateProviderIdErrorComponent
        | ApiV1BlockRolloutItemsUpdateProviderReferenceErrorComponent
        | ApiV1BlockRolloutItemsUpdateReasonErrorComponent
        | ApiV1BlockRolloutItemsUpdateReconciliationEnabledErrorComponent
        | ApiV1BlockRolloutItemsUpdateReconciliationRunningErrorComponent
        | ApiV1BlockRolloutItemsUpdateReconciliationTaskIdErrorComponent
        | ApiV1BlockRolloutItemsUpdateReconciliationTaskMetaErrorComponent
        | ApiV1BlockRolloutItemsUpdateRepairRunningErrorComponent
        | ApiV1BlockRolloutItemsUpdateRepairTaskIdErrorComponent
        | ApiV1BlockRolloutItemsUpdateRepairTaskMetaErrorComponent
        | ApiV1BlockRolloutItemsUpdateRolloutErrorComponent
        | ApiV1BlockRolloutItemsUpdateScopeErrorComponent
        | ApiV1BlockRolloutItemsUpdateSlaAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsUpdateSlaTargetErrorComponent
        | ApiV1BlockRolloutItemsUpdateSloAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsUpdateSloTargetErrorComponent
        | ApiV1BlockRolloutItemsUpdateSourceErrorComponent
        | ApiV1BlockRolloutItemsUpdateSourceUserErrorComponent
        | ApiV1BlockRolloutItemsUpdateStateErrorComponent
        | ApiV1BlockRolloutItemsUpdateStateReasonErrorComponent
        | ApiV1BlockRolloutItemsUpdateStatusErrorComponent
        | ApiV1BlockRolloutItemsUpdateTargetAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_block_rollout_items_update_action_name_error_component import (
            ApiV1BlockRolloutItemsUpdateActionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_action_run_error_component import (
            ApiV1BlockRolloutItemsUpdateActionRunErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_actual_availability_error_component import (
            ApiV1BlockRolloutItemsUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_annotations_error_component import (
            ApiV1BlockRolloutItemsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_archived_at_error_component import (
            ApiV1BlockRolloutItemsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_archived_error_component import (
            ApiV1BlockRolloutItemsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_archived_reason_error_component import (
            ApiV1BlockRolloutItemsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_block_error_component import (
            ApiV1BlockRolloutItemsUpdateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_conditions_error_component import (
            ApiV1BlockRolloutItemsUpdateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_criticality_error_component import (
            ApiV1BlockRolloutItemsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_debug_mode_error_component import (
            ApiV1BlockRolloutItemsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_discovery_enabled_error_component import (
            ApiV1BlockRolloutItemsUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_discovery_running_error_component import (
            ApiV1BlockRolloutItemsUpdateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_discovery_task_id_error_component import (
            ApiV1BlockRolloutItemsUpdateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_discovery_task_meta_error_component import (
            ApiV1BlockRolloutItemsUpdateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_display_name_error_component import (
            ApiV1BlockRolloutItemsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_kind_error_component import (
            ApiV1BlockRolloutItemsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_labels_error_component import (
            ApiV1BlockRolloutItemsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_last_state_change_error_component import (
            ApiV1BlockRolloutItemsUpdateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_last_state_error_component import (
            ApiV1BlockRolloutItemsUpdateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_name_error_component import (
            ApiV1BlockRolloutItemsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_non_field_errors_error_component import (
            ApiV1BlockRolloutItemsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_platform_service_error_component import (
            ApiV1BlockRolloutItemsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_provider_error_component import (
            ApiV1BlockRolloutItemsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_provider_id_error_component import (
            ApiV1BlockRolloutItemsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_provider_reference_error_component import (
            ApiV1BlockRolloutItemsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutItemsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_reconciliation_running_error_component import (
            ApiV1BlockRolloutItemsUpdateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutItemsUpdateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutItemsUpdateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_repair_running_error_component import (
            ApiV1BlockRolloutItemsUpdateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_repair_task_id_error_component import (
            ApiV1BlockRolloutItemsUpdateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_repair_task_meta_error_component import (
            ApiV1BlockRolloutItemsUpdateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_rollout_error_component import (
            ApiV1BlockRolloutItemsUpdateRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_scope_error_component import (
            ApiV1BlockRolloutItemsUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_sla_availability_error_component import (
            ApiV1BlockRolloutItemsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_sla_target_error_component import (
            ApiV1BlockRolloutItemsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_slo_availability_error_component import (
            ApiV1BlockRolloutItemsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_slo_target_error_component import (
            ApiV1BlockRolloutItemsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_source_error_component import (
            ApiV1BlockRolloutItemsUpdateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_source_user_error_component import (
            ApiV1BlockRolloutItemsUpdateSourceUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_state_error_component import (
            ApiV1BlockRolloutItemsUpdateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_state_reason_error_component import (
            ApiV1BlockRolloutItemsUpdateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_status_error_component import (
            ApiV1BlockRolloutItemsUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_target_availability_error_component import (
            ApiV1BlockRolloutItemsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_tolerations_error_component import (
            ApiV1BlockRolloutItemsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateReconciliationTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateActionNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateSourceUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateRolloutErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsUpdateActionRunErrorComponent):
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
        from ..models.api_v1_block_rollout_items_update_action_name_error_component import (
            ApiV1BlockRolloutItemsUpdateActionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_action_run_error_component import (
            ApiV1BlockRolloutItemsUpdateActionRunErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_actual_availability_error_component import (
            ApiV1BlockRolloutItemsUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_annotations_error_component import (
            ApiV1BlockRolloutItemsUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_archived_at_error_component import (
            ApiV1BlockRolloutItemsUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_archived_error_component import (
            ApiV1BlockRolloutItemsUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_archived_reason_error_component import (
            ApiV1BlockRolloutItemsUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_block_error_component import (
            ApiV1BlockRolloutItemsUpdateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_conditions_error_component import (
            ApiV1BlockRolloutItemsUpdateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_criticality_error_component import (
            ApiV1BlockRolloutItemsUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_debug_mode_error_component import (
            ApiV1BlockRolloutItemsUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_discovery_enabled_error_component import (
            ApiV1BlockRolloutItemsUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_discovery_running_error_component import (
            ApiV1BlockRolloutItemsUpdateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_discovery_task_id_error_component import (
            ApiV1BlockRolloutItemsUpdateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_discovery_task_meta_error_component import (
            ApiV1BlockRolloutItemsUpdateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_display_name_error_component import (
            ApiV1BlockRolloutItemsUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_kind_error_component import (
            ApiV1BlockRolloutItemsUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_labels_error_component import (
            ApiV1BlockRolloutItemsUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_last_state_change_error_component import (
            ApiV1BlockRolloutItemsUpdateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_last_state_error_component import (
            ApiV1BlockRolloutItemsUpdateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_name_error_component import (
            ApiV1BlockRolloutItemsUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_non_field_errors_error_component import (
            ApiV1BlockRolloutItemsUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_platform_service_error_component import (
            ApiV1BlockRolloutItemsUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_provider_error_component import (
            ApiV1BlockRolloutItemsUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_provider_id_error_component import (
            ApiV1BlockRolloutItemsUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_provider_reference_error_component import (
            ApiV1BlockRolloutItemsUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_reason_error_component import (
            ApiV1BlockRolloutItemsUpdateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutItemsUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_reconciliation_running_error_component import (
            ApiV1BlockRolloutItemsUpdateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutItemsUpdateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutItemsUpdateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_repair_running_error_component import (
            ApiV1BlockRolloutItemsUpdateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_repair_task_id_error_component import (
            ApiV1BlockRolloutItemsUpdateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_repair_task_meta_error_component import (
            ApiV1BlockRolloutItemsUpdateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_rollout_error_component import (
            ApiV1BlockRolloutItemsUpdateRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_scope_error_component import (
            ApiV1BlockRolloutItemsUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_sla_availability_error_component import (
            ApiV1BlockRolloutItemsUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_sla_target_error_component import (
            ApiV1BlockRolloutItemsUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_slo_availability_error_component import (
            ApiV1BlockRolloutItemsUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_slo_target_error_component import (
            ApiV1BlockRolloutItemsUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_source_error_component import (
            ApiV1BlockRolloutItemsUpdateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_source_user_error_component import (
            ApiV1BlockRolloutItemsUpdateSourceUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_state_error_component import (
            ApiV1BlockRolloutItemsUpdateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_state_reason_error_component import (
            ApiV1BlockRolloutItemsUpdateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_status_error_component import (
            ApiV1BlockRolloutItemsUpdateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_target_availability_error_component import (
            ApiV1BlockRolloutItemsUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_update_tolerations_error_component import (
            ApiV1BlockRolloutItemsUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlockRolloutItemsUpdateActionNameErrorComponent
                | ApiV1BlockRolloutItemsUpdateActionRunErrorComponent
                | ApiV1BlockRolloutItemsUpdateActualAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsUpdateAnnotationsErrorComponent
                | ApiV1BlockRolloutItemsUpdateArchivedAtErrorComponent
                | ApiV1BlockRolloutItemsUpdateArchivedErrorComponent
                | ApiV1BlockRolloutItemsUpdateArchivedReasonErrorComponent
                | ApiV1BlockRolloutItemsUpdateBlockErrorComponent
                | ApiV1BlockRolloutItemsUpdateConditionsErrorComponent
                | ApiV1BlockRolloutItemsUpdateCriticalityErrorComponent
                | ApiV1BlockRolloutItemsUpdateDebugModeErrorComponent
                | ApiV1BlockRolloutItemsUpdateDiscoveryEnabledErrorComponent
                | ApiV1BlockRolloutItemsUpdateDiscoveryRunningErrorComponent
                | ApiV1BlockRolloutItemsUpdateDiscoveryTaskIdErrorComponent
                | ApiV1BlockRolloutItemsUpdateDiscoveryTaskMetaErrorComponent
                | ApiV1BlockRolloutItemsUpdateDisplayNameErrorComponent
                | ApiV1BlockRolloutItemsUpdateKindErrorComponent
                | ApiV1BlockRolloutItemsUpdateLabelsErrorComponent
                | ApiV1BlockRolloutItemsUpdateLastStateChangeErrorComponent
                | ApiV1BlockRolloutItemsUpdateLastStateErrorComponent
                | ApiV1BlockRolloutItemsUpdateNameErrorComponent
                | ApiV1BlockRolloutItemsUpdateNonFieldErrorsErrorComponent
                | ApiV1BlockRolloutItemsUpdatePlatformServiceErrorComponent
                | ApiV1BlockRolloutItemsUpdateProviderErrorComponent
                | ApiV1BlockRolloutItemsUpdateProviderIdErrorComponent
                | ApiV1BlockRolloutItemsUpdateProviderReferenceErrorComponent
                | ApiV1BlockRolloutItemsUpdateReasonErrorComponent
                | ApiV1BlockRolloutItemsUpdateReconciliationEnabledErrorComponent
                | ApiV1BlockRolloutItemsUpdateReconciliationRunningErrorComponent
                | ApiV1BlockRolloutItemsUpdateReconciliationTaskIdErrorComponent
                | ApiV1BlockRolloutItemsUpdateReconciliationTaskMetaErrorComponent
                | ApiV1BlockRolloutItemsUpdateRepairRunningErrorComponent
                | ApiV1BlockRolloutItemsUpdateRepairTaskIdErrorComponent
                | ApiV1BlockRolloutItemsUpdateRepairTaskMetaErrorComponent
                | ApiV1BlockRolloutItemsUpdateRolloutErrorComponent
                | ApiV1BlockRolloutItemsUpdateScopeErrorComponent
                | ApiV1BlockRolloutItemsUpdateSlaAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsUpdateSlaTargetErrorComponent
                | ApiV1BlockRolloutItemsUpdateSloAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsUpdateSloTargetErrorComponent
                | ApiV1BlockRolloutItemsUpdateSourceErrorComponent
                | ApiV1BlockRolloutItemsUpdateSourceUserErrorComponent
                | ApiV1BlockRolloutItemsUpdateStateErrorComponent
                | ApiV1BlockRolloutItemsUpdateStateReasonErrorComponent
                | ApiV1BlockRolloutItemsUpdateStatusErrorComponent
                | ApiV1BlockRolloutItemsUpdateTargetAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_0 = (
                        ApiV1BlockRolloutItemsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_1 = (
                        ApiV1BlockRolloutItemsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_2 = (
                        ApiV1BlockRolloutItemsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_3 = (
                        ApiV1BlockRolloutItemsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_4 = (
                        ApiV1BlockRolloutItemsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_5 = (
                        ApiV1BlockRolloutItemsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_6 = (
                        ApiV1BlockRolloutItemsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_7 = (
                        ApiV1BlockRolloutItemsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_8 = (
                        ApiV1BlockRolloutItemsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_9 = (
                        ApiV1BlockRolloutItemsUpdateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_10 = (
                        ApiV1BlockRolloutItemsUpdateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_11 = (
                        ApiV1BlockRolloutItemsUpdateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_12 = (
                        ApiV1BlockRolloutItemsUpdateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_13 = (
                        ApiV1BlockRolloutItemsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_14 = (
                        ApiV1BlockRolloutItemsUpdateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_15 = (
                        ApiV1BlockRolloutItemsUpdateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_16 = (
                        ApiV1BlockRolloutItemsUpdateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_17 = (
                        ApiV1BlockRolloutItemsUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_18 = (
                        ApiV1BlockRolloutItemsUpdateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_19 = (
                        ApiV1BlockRolloutItemsUpdateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_20 = (
                        ApiV1BlockRolloutItemsUpdateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_21 = (
                        ApiV1BlockRolloutItemsUpdateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_22 = (
                        ApiV1BlockRolloutItemsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_23 = (
                        ApiV1BlockRolloutItemsUpdateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_24 = (
                        ApiV1BlockRolloutItemsUpdateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_25 = (
                        ApiV1BlockRolloutItemsUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_26 = (
                        ApiV1BlockRolloutItemsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_27 = (
                        ApiV1BlockRolloutItemsUpdateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_28 = (
                        ApiV1BlockRolloutItemsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_29 = (
                        ApiV1BlockRolloutItemsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_30 = (
                        ApiV1BlockRolloutItemsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_31 = (
                        ApiV1BlockRolloutItemsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_32 = (
                        ApiV1BlockRolloutItemsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_33 = (
                        ApiV1BlockRolloutItemsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_34 = (
                        ApiV1BlockRolloutItemsUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_35 = (
                        ApiV1BlockRolloutItemsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_36 = (
                        ApiV1BlockRolloutItemsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_37 = (
                        ApiV1BlockRolloutItemsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_38 = (
                        ApiV1BlockRolloutItemsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_39 = (
                        ApiV1BlockRolloutItemsUpdateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_40 = (
                        ApiV1BlockRolloutItemsUpdateActionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_41 = (
                        ApiV1BlockRolloutItemsUpdateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_42 = (
                        ApiV1BlockRolloutItemsUpdateSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_43 = (
                        ApiV1BlockRolloutItemsUpdateSourceUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_44 = (
                        ApiV1BlockRolloutItemsUpdateRolloutErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_update_error_type_45 = (
                        ApiV1BlockRolloutItemsUpdateActionRunErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_update_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_block_rollout_items_update_error_type_46 = (
                    ApiV1BlockRolloutItemsUpdateReasonErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_block_rollout_items_update_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_block_rollout_items_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_block_rollout_items_update_validation_error.additional_properties = d
        return api_v1_block_rollout_items_update_validation_error

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
