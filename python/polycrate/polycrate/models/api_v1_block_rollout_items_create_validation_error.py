from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_block_rollout_items_create_action_name_error_component import (
        ApiV1BlockRolloutItemsCreateActionNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_action_run_error_component import (
        ApiV1BlockRolloutItemsCreateActionRunErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_actual_availability_error_component import (
        ApiV1BlockRolloutItemsCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_annotations_error_component import (
        ApiV1BlockRolloutItemsCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_archived_at_error_component import (
        ApiV1BlockRolloutItemsCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_archived_error_component import (
        ApiV1BlockRolloutItemsCreateArchivedErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_archived_reason_error_component import (
        ApiV1BlockRolloutItemsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_block_error_component import (
        ApiV1BlockRolloutItemsCreateBlockErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_conditions_error_component import (
        ApiV1BlockRolloutItemsCreateConditionsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_criticality_error_component import (
        ApiV1BlockRolloutItemsCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_debug_mode_error_component import (
        ApiV1BlockRolloutItemsCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_discovery_enabled_error_component import (
        ApiV1BlockRolloutItemsCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_discovery_running_error_component import (
        ApiV1BlockRolloutItemsCreateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_discovery_task_id_error_component import (
        ApiV1BlockRolloutItemsCreateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_discovery_task_meta_error_component import (
        ApiV1BlockRolloutItemsCreateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_display_name_error_component import (
        ApiV1BlockRolloutItemsCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_kind_error_component import (
        ApiV1BlockRolloutItemsCreateKindErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_labels_error_component import (
        ApiV1BlockRolloutItemsCreateLabelsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_last_state_change_error_component import (
        ApiV1BlockRolloutItemsCreateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_last_state_error_component import (
        ApiV1BlockRolloutItemsCreateLastStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_name_error_component import (
        ApiV1BlockRolloutItemsCreateNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_non_field_errors_error_component import (
        ApiV1BlockRolloutItemsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_platform_service_error_component import (
        ApiV1BlockRolloutItemsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_provider_error_component import (
        ApiV1BlockRolloutItemsCreateProviderErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_provider_id_error_component import (
        ApiV1BlockRolloutItemsCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_provider_reference_error_component import (
        ApiV1BlockRolloutItemsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_reason_error_component import (
        ApiV1BlockRolloutItemsCreateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_reconciliation_enabled_error_component import (
        ApiV1BlockRolloutItemsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_reconciliation_running_error_component import (
        ApiV1BlockRolloutItemsCreateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_reconciliation_task_id_error_component import (
        ApiV1BlockRolloutItemsCreateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_reconciliation_task_meta_error_component import (
        ApiV1BlockRolloutItemsCreateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_repair_running_error_component import (
        ApiV1BlockRolloutItemsCreateRepairRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_repair_task_id_error_component import (
        ApiV1BlockRolloutItemsCreateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_repair_task_meta_error_component import (
        ApiV1BlockRolloutItemsCreateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_rollout_error_component import (
        ApiV1BlockRolloutItemsCreateRolloutErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_scope_error_component import (
        ApiV1BlockRolloutItemsCreateScopeErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_sla_availability_error_component import (
        ApiV1BlockRolloutItemsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_sla_target_error_component import (
        ApiV1BlockRolloutItemsCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_slo_availability_error_component import (
        ApiV1BlockRolloutItemsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_slo_target_error_component import (
        ApiV1BlockRolloutItemsCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_source_error_component import (
        ApiV1BlockRolloutItemsCreateSourceErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_source_user_error_component import (
        ApiV1BlockRolloutItemsCreateSourceUserErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_state_error_component import (
        ApiV1BlockRolloutItemsCreateStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_state_reason_error_component import (
        ApiV1BlockRolloutItemsCreateStateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_status_error_component import (
        ApiV1BlockRolloutItemsCreateStatusErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_target_availability_error_component import (
        ApiV1BlockRolloutItemsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_create_tolerations_error_component import (
        ApiV1BlockRolloutItemsCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlockRolloutItemsCreateValidationError")


@_attrs_define
class ApiV1BlockRolloutItemsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlockRolloutItemsCreateActionNameErrorComponent |
            ApiV1BlockRolloutItemsCreateActionRunErrorComponent |
            ApiV1BlockRolloutItemsCreateActualAvailabilityErrorComponent |
            ApiV1BlockRolloutItemsCreateAnnotationsErrorComponent | ApiV1BlockRolloutItemsCreateArchivedAtErrorComponent |
            ApiV1BlockRolloutItemsCreateArchivedErrorComponent | ApiV1BlockRolloutItemsCreateArchivedReasonErrorComponent |
            ApiV1BlockRolloutItemsCreateBlockErrorComponent | ApiV1BlockRolloutItemsCreateConditionsErrorComponent |
            ApiV1BlockRolloutItemsCreateCriticalityErrorComponent | ApiV1BlockRolloutItemsCreateDebugModeErrorComponent |
            ApiV1BlockRolloutItemsCreateDiscoveryEnabledErrorComponent |
            ApiV1BlockRolloutItemsCreateDiscoveryRunningErrorComponent |
            ApiV1BlockRolloutItemsCreateDiscoveryTaskIdErrorComponent |
            ApiV1BlockRolloutItemsCreateDiscoveryTaskMetaErrorComponent |
            ApiV1BlockRolloutItemsCreateDisplayNameErrorComponent | ApiV1BlockRolloutItemsCreateKindErrorComponent |
            ApiV1BlockRolloutItemsCreateLabelsErrorComponent | ApiV1BlockRolloutItemsCreateLastStateChangeErrorComponent |
            ApiV1BlockRolloutItemsCreateLastStateErrorComponent | ApiV1BlockRolloutItemsCreateNameErrorComponent |
            ApiV1BlockRolloutItemsCreateNonFieldErrorsErrorComponent |
            ApiV1BlockRolloutItemsCreatePlatformServiceErrorComponent | ApiV1BlockRolloutItemsCreateProviderErrorComponent |
            ApiV1BlockRolloutItemsCreateProviderIdErrorComponent |
            ApiV1BlockRolloutItemsCreateProviderReferenceErrorComponent | ApiV1BlockRolloutItemsCreateReasonErrorComponent |
            ApiV1BlockRolloutItemsCreateReconciliationEnabledErrorComponent |
            ApiV1BlockRolloutItemsCreateReconciliationRunningErrorComponent |
            ApiV1BlockRolloutItemsCreateReconciliationTaskIdErrorComponent |
            ApiV1BlockRolloutItemsCreateReconciliationTaskMetaErrorComponent |
            ApiV1BlockRolloutItemsCreateRepairRunningErrorComponent | ApiV1BlockRolloutItemsCreateRepairTaskIdErrorComponent
            | ApiV1BlockRolloutItemsCreateRepairTaskMetaErrorComponent | ApiV1BlockRolloutItemsCreateRolloutErrorComponent |
            ApiV1BlockRolloutItemsCreateScopeErrorComponent | ApiV1BlockRolloutItemsCreateSlaAvailabilityErrorComponent |
            ApiV1BlockRolloutItemsCreateSlaTargetErrorComponent | ApiV1BlockRolloutItemsCreateSloAvailabilityErrorComponent
            | ApiV1BlockRolloutItemsCreateSloTargetErrorComponent | ApiV1BlockRolloutItemsCreateSourceErrorComponent |
            ApiV1BlockRolloutItemsCreateSourceUserErrorComponent | ApiV1BlockRolloutItemsCreateStateErrorComponent |
            ApiV1BlockRolloutItemsCreateStateReasonErrorComponent | ApiV1BlockRolloutItemsCreateStatusErrorComponent |
            ApiV1BlockRolloutItemsCreateTargetAvailabilityErrorComponent |
            ApiV1BlockRolloutItemsCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlockRolloutItemsCreateActionNameErrorComponent
        | ApiV1BlockRolloutItemsCreateActionRunErrorComponent
        | ApiV1BlockRolloutItemsCreateActualAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsCreateAnnotationsErrorComponent
        | ApiV1BlockRolloutItemsCreateArchivedAtErrorComponent
        | ApiV1BlockRolloutItemsCreateArchivedErrorComponent
        | ApiV1BlockRolloutItemsCreateArchivedReasonErrorComponent
        | ApiV1BlockRolloutItemsCreateBlockErrorComponent
        | ApiV1BlockRolloutItemsCreateConditionsErrorComponent
        | ApiV1BlockRolloutItemsCreateCriticalityErrorComponent
        | ApiV1BlockRolloutItemsCreateDebugModeErrorComponent
        | ApiV1BlockRolloutItemsCreateDiscoveryEnabledErrorComponent
        | ApiV1BlockRolloutItemsCreateDiscoveryRunningErrorComponent
        | ApiV1BlockRolloutItemsCreateDiscoveryTaskIdErrorComponent
        | ApiV1BlockRolloutItemsCreateDiscoveryTaskMetaErrorComponent
        | ApiV1BlockRolloutItemsCreateDisplayNameErrorComponent
        | ApiV1BlockRolloutItemsCreateKindErrorComponent
        | ApiV1BlockRolloutItemsCreateLabelsErrorComponent
        | ApiV1BlockRolloutItemsCreateLastStateChangeErrorComponent
        | ApiV1BlockRolloutItemsCreateLastStateErrorComponent
        | ApiV1BlockRolloutItemsCreateNameErrorComponent
        | ApiV1BlockRolloutItemsCreateNonFieldErrorsErrorComponent
        | ApiV1BlockRolloutItemsCreatePlatformServiceErrorComponent
        | ApiV1BlockRolloutItemsCreateProviderErrorComponent
        | ApiV1BlockRolloutItemsCreateProviderIdErrorComponent
        | ApiV1BlockRolloutItemsCreateProviderReferenceErrorComponent
        | ApiV1BlockRolloutItemsCreateReasonErrorComponent
        | ApiV1BlockRolloutItemsCreateReconciliationEnabledErrorComponent
        | ApiV1BlockRolloutItemsCreateReconciliationRunningErrorComponent
        | ApiV1BlockRolloutItemsCreateReconciliationTaskIdErrorComponent
        | ApiV1BlockRolloutItemsCreateReconciliationTaskMetaErrorComponent
        | ApiV1BlockRolloutItemsCreateRepairRunningErrorComponent
        | ApiV1BlockRolloutItemsCreateRepairTaskIdErrorComponent
        | ApiV1BlockRolloutItemsCreateRepairTaskMetaErrorComponent
        | ApiV1BlockRolloutItemsCreateRolloutErrorComponent
        | ApiV1BlockRolloutItemsCreateScopeErrorComponent
        | ApiV1BlockRolloutItemsCreateSlaAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsCreateSlaTargetErrorComponent
        | ApiV1BlockRolloutItemsCreateSloAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsCreateSloTargetErrorComponent
        | ApiV1BlockRolloutItemsCreateSourceErrorComponent
        | ApiV1BlockRolloutItemsCreateSourceUserErrorComponent
        | ApiV1BlockRolloutItemsCreateStateErrorComponent
        | ApiV1BlockRolloutItemsCreateStateReasonErrorComponent
        | ApiV1BlockRolloutItemsCreateStatusErrorComponent
        | ApiV1BlockRolloutItemsCreateTargetAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_block_rollout_items_create_action_name_error_component import (
            ApiV1BlockRolloutItemsCreateActionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_action_run_error_component import (
            ApiV1BlockRolloutItemsCreateActionRunErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_actual_availability_error_component import (
            ApiV1BlockRolloutItemsCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_annotations_error_component import (
            ApiV1BlockRolloutItemsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_archived_at_error_component import (
            ApiV1BlockRolloutItemsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_archived_error_component import (
            ApiV1BlockRolloutItemsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_archived_reason_error_component import (
            ApiV1BlockRolloutItemsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_block_error_component import (
            ApiV1BlockRolloutItemsCreateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_conditions_error_component import (
            ApiV1BlockRolloutItemsCreateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_criticality_error_component import (
            ApiV1BlockRolloutItemsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_debug_mode_error_component import (
            ApiV1BlockRolloutItemsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_discovery_enabled_error_component import (
            ApiV1BlockRolloutItemsCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_discovery_running_error_component import (
            ApiV1BlockRolloutItemsCreateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_discovery_task_id_error_component import (
            ApiV1BlockRolloutItemsCreateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_discovery_task_meta_error_component import (
            ApiV1BlockRolloutItemsCreateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_display_name_error_component import (
            ApiV1BlockRolloutItemsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_kind_error_component import (
            ApiV1BlockRolloutItemsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_labels_error_component import (
            ApiV1BlockRolloutItemsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_last_state_change_error_component import (
            ApiV1BlockRolloutItemsCreateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_last_state_error_component import (
            ApiV1BlockRolloutItemsCreateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_name_error_component import (
            ApiV1BlockRolloutItemsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_non_field_errors_error_component import (
            ApiV1BlockRolloutItemsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_platform_service_error_component import (
            ApiV1BlockRolloutItemsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_provider_error_component import (
            ApiV1BlockRolloutItemsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_provider_id_error_component import (
            ApiV1BlockRolloutItemsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_provider_reference_error_component import (
            ApiV1BlockRolloutItemsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutItemsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_reconciliation_running_error_component import (
            ApiV1BlockRolloutItemsCreateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutItemsCreateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutItemsCreateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_repair_running_error_component import (
            ApiV1BlockRolloutItemsCreateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_repair_task_id_error_component import (
            ApiV1BlockRolloutItemsCreateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_repair_task_meta_error_component import (
            ApiV1BlockRolloutItemsCreateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_rollout_error_component import (
            ApiV1BlockRolloutItemsCreateRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_scope_error_component import (
            ApiV1BlockRolloutItemsCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_sla_availability_error_component import (
            ApiV1BlockRolloutItemsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_sla_target_error_component import (
            ApiV1BlockRolloutItemsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_slo_availability_error_component import (
            ApiV1BlockRolloutItemsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_slo_target_error_component import (
            ApiV1BlockRolloutItemsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_source_error_component import (
            ApiV1BlockRolloutItemsCreateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_source_user_error_component import (
            ApiV1BlockRolloutItemsCreateSourceUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_state_error_component import (
            ApiV1BlockRolloutItemsCreateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_state_reason_error_component import (
            ApiV1BlockRolloutItemsCreateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_status_error_component import (
            ApiV1BlockRolloutItemsCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_target_availability_error_component import (
            ApiV1BlockRolloutItemsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_tolerations_error_component import (
            ApiV1BlockRolloutItemsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateReconciliationTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateActionNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateSourceUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateRolloutErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsCreateActionRunErrorComponent):
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
        from ..models.api_v1_block_rollout_items_create_action_name_error_component import (
            ApiV1BlockRolloutItemsCreateActionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_action_run_error_component import (
            ApiV1BlockRolloutItemsCreateActionRunErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_actual_availability_error_component import (
            ApiV1BlockRolloutItemsCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_annotations_error_component import (
            ApiV1BlockRolloutItemsCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_archived_at_error_component import (
            ApiV1BlockRolloutItemsCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_archived_error_component import (
            ApiV1BlockRolloutItemsCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_archived_reason_error_component import (
            ApiV1BlockRolloutItemsCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_block_error_component import (
            ApiV1BlockRolloutItemsCreateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_conditions_error_component import (
            ApiV1BlockRolloutItemsCreateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_criticality_error_component import (
            ApiV1BlockRolloutItemsCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_debug_mode_error_component import (
            ApiV1BlockRolloutItemsCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_discovery_enabled_error_component import (
            ApiV1BlockRolloutItemsCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_discovery_running_error_component import (
            ApiV1BlockRolloutItemsCreateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_discovery_task_id_error_component import (
            ApiV1BlockRolloutItemsCreateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_discovery_task_meta_error_component import (
            ApiV1BlockRolloutItemsCreateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_display_name_error_component import (
            ApiV1BlockRolloutItemsCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_kind_error_component import (
            ApiV1BlockRolloutItemsCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_labels_error_component import (
            ApiV1BlockRolloutItemsCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_last_state_change_error_component import (
            ApiV1BlockRolloutItemsCreateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_last_state_error_component import (
            ApiV1BlockRolloutItemsCreateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_name_error_component import (
            ApiV1BlockRolloutItemsCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_non_field_errors_error_component import (
            ApiV1BlockRolloutItemsCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_platform_service_error_component import (
            ApiV1BlockRolloutItemsCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_provider_error_component import (
            ApiV1BlockRolloutItemsCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_provider_id_error_component import (
            ApiV1BlockRolloutItemsCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_provider_reference_error_component import (
            ApiV1BlockRolloutItemsCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_reason_error_component import (
            ApiV1BlockRolloutItemsCreateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutItemsCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_reconciliation_running_error_component import (
            ApiV1BlockRolloutItemsCreateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutItemsCreateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutItemsCreateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_repair_running_error_component import (
            ApiV1BlockRolloutItemsCreateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_repair_task_id_error_component import (
            ApiV1BlockRolloutItemsCreateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_repair_task_meta_error_component import (
            ApiV1BlockRolloutItemsCreateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_rollout_error_component import (
            ApiV1BlockRolloutItemsCreateRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_scope_error_component import (
            ApiV1BlockRolloutItemsCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_sla_availability_error_component import (
            ApiV1BlockRolloutItemsCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_sla_target_error_component import (
            ApiV1BlockRolloutItemsCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_slo_availability_error_component import (
            ApiV1BlockRolloutItemsCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_slo_target_error_component import (
            ApiV1BlockRolloutItemsCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_source_error_component import (
            ApiV1BlockRolloutItemsCreateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_source_user_error_component import (
            ApiV1BlockRolloutItemsCreateSourceUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_state_error_component import (
            ApiV1BlockRolloutItemsCreateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_state_reason_error_component import (
            ApiV1BlockRolloutItemsCreateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_status_error_component import (
            ApiV1BlockRolloutItemsCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_target_availability_error_component import (
            ApiV1BlockRolloutItemsCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_create_tolerations_error_component import (
            ApiV1BlockRolloutItemsCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlockRolloutItemsCreateActionNameErrorComponent
                | ApiV1BlockRolloutItemsCreateActionRunErrorComponent
                | ApiV1BlockRolloutItemsCreateActualAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsCreateAnnotationsErrorComponent
                | ApiV1BlockRolloutItemsCreateArchivedAtErrorComponent
                | ApiV1BlockRolloutItemsCreateArchivedErrorComponent
                | ApiV1BlockRolloutItemsCreateArchivedReasonErrorComponent
                | ApiV1BlockRolloutItemsCreateBlockErrorComponent
                | ApiV1BlockRolloutItemsCreateConditionsErrorComponent
                | ApiV1BlockRolloutItemsCreateCriticalityErrorComponent
                | ApiV1BlockRolloutItemsCreateDebugModeErrorComponent
                | ApiV1BlockRolloutItemsCreateDiscoveryEnabledErrorComponent
                | ApiV1BlockRolloutItemsCreateDiscoveryRunningErrorComponent
                | ApiV1BlockRolloutItemsCreateDiscoveryTaskIdErrorComponent
                | ApiV1BlockRolloutItemsCreateDiscoveryTaskMetaErrorComponent
                | ApiV1BlockRolloutItemsCreateDisplayNameErrorComponent
                | ApiV1BlockRolloutItemsCreateKindErrorComponent
                | ApiV1BlockRolloutItemsCreateLabelsErrorComponent
                | ApiV1BlockRolloutItemsCreateLastStateChangeErrorComponent
                | ApiV1BlockRolloutItemsCreateLastStateErrorComponent
                | ApiV1BlockRolloutItemsCreateNameErrorComponent
                | ApiV1BlockRolloutItemsCreateNonFieldErrorsErrorComponent
                | ApiV1BlockRolloutItemsCreatePlatformServiceErrorComponent
                | ApiV1BlockRolloutItemsCreateProviderErrorComponent
                | ApiV1BlockRolloutItemsCreateProviderIdErrorComponent
                | ApiV1BlockRolloutItemsCreateProviderReferenceErrorComponent
                | ApiV1BlockRolloutItemsCreateReasonErrorComponent
                | ApiV1BlockRolloutItemsCreateReconciliationEnabledErrorComponent
                | ApiV1BlockRolloutItemsCreateReconciliationRunningErrorComponent
                | ApiV1BlockRolloutItemsCreateReconciliationTaskIdErrorComponent
                | ApiV1BlockRolloutItemsCreateReconciliationTaskMetaErrorComponent
                | ApiV1BlockRolloutItemsCreateRepairRunningErrorComponent
                | ApiV1BlockRolloutItemsCreateRepairTaskIdErrorComponent
                | ApiV1BlockRolloutItemsCreateRepairTaskMetaErrorComponent
                | ApiV1BlockRolloutItemsCreateRolloutErrorComponent
                | ApiV1BlockRolloutItemsCreateScopeErrorComponent
                | ApiV1BlockRolloutItemsCreateSlaAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsCreateSlaTargetErrorComponent
                | ApiV1BlockRolloutItemsCreateSloAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsCreateSloTargetErrorComponent
                | ApiV1BlockRolloutItemsCreateSourceErrorComponent
                | ApiV1BlockRolloutItemsCreateSourceUserErrorComponent
                | ApiV1BlockRolloutItemsCreateStateErrorComponent
                | ApiV1BlockRolloutItemsCreateStateReasonErrorComponent
                | ApiV1BlockRolloutItemsCreateStatusErrorComponent
                | ApiV1BlockRolloutItemsCreateTargetAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_0 = (
                        ApiV1BlockRolloutItemsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_1 = (
                        ApiV1BlockRolloutItemsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_2 = (
                        ApiV1BlockRolloutItemsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_3 = (
                        ApiV1BlockRolloutItemsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_4 = (
                        ApiV1BlockRolloutItemsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_5 = (
                        ApiV1BlockRolloutItemsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_6 = (
                        ApiV1BlockRolloutItemsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_7 = (
                        ApiV1BlockRolloutItemsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_8 = (
                        ApiV1BlockRolloutItemsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_9 = (
                        ApiV1BlockRolloutItemsCreateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_10 = (
                        ApiV1BlockRolloutItemsCreateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_11 = (
                        ApiV1BlockRolloutItemsCreateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_12 = (
                        ApiV1BlockRolloutItemsCreateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_13 = (
                        ApiV1BlockRolloutItemsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_14 = (
                        ApiV1BlockRolloutItemsCreateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_15 = (
                        ApiV1BlockRolloutItemsCreateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_16 = (
                        ApiV1BlockRolloutItemsCreateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_17 = (
                        ApiV1BlockRolloutItemsCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_18 = (
                        ApiV1BlockRolloutItemsCreateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_19 = (
                        ApiV1BlockRolloutItemsCreateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_20 = (
                        ApiV1BlockRolloutItemsCreateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_21 = (
                        ApiV1BlockRolloutItemsCreateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_22 = (
                        ApiV1BlockRolloutItemsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_23 = (
                        ApiV1BlockRolloutItemsCreateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_24 = (
                        ApiV1BlockRolloutItemsCreateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_25 = (
                        ApiV1BlockRolloutItemsCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_26 = (
                        ApiV1BlockRolloutItemsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_27 = (
                        ApiV1BlockRolloutItemsCreateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_28 = (
                        ApiV1BlockRolloutItemsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_29 = (
                        ApiV1BlockRolloutItemsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_30 = (
                        ApiV1BlockRolloutItemsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_31 = (
                        ApiV1BlockRolloutItemsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_32 = (
                        ApiV1BlockRolloutItemsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_33 = (
                        ApiV1BlockRolloutItemsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_34 = (
                        ApiV1BlockRolloutItemsCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_35 = (
                        ApiV1BlockRolloutItemsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_36 = (
                        ApiV1BlockRolloutItemsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_37 = (
                        ApiV1BlockRolloutItemsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_38 = (
                        ApiV1BlockRolloutItemsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_39 = (
                        ApiV1BlockRolloutItemsCreateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_40 = (
                        ApiV1BlockRolloutItemsCreateActionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_41 = (
                        ApiV1BlockRolloutItemsCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_42 = (
                        ApiV1BlockRolloutItemsCreateSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_43 = (
                        ApiV1BlockRolloutItemsCreateSourceUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_44 = (
                        ApiV1BlockRolloutItemsCreateRolloutErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_create_error_type_45 = (
                        ApiV1BlockRolloutItemsCreateActionRunErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_block_rollout_items_create_error_type_46 = (
                    ApiV1BlockRolloutItemsCreateReasonErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_block_rollout_items_create_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_block_rollout_items_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_block_rollout_items_create_validation_error.additional_properties = d
        return api_v1_block_rollout_items_create_validation_error

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
