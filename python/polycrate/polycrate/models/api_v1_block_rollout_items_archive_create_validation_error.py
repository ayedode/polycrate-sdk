from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_block_rollout_items_archive_create_action_name_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateActionNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_action_run_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateActionRunErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_actual_availability_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_annotations_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_archived_at_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_archived_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateArchivedErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_archived_reason_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_block_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateBlockErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_conditions_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateConditionsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_criticality_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_debug_mode_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_discovery_enabled_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_discovery_running_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_discovery_task_id_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_discovery_task_meta_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_display_name_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_kind_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateKindErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_labels_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateLabelsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_last_state_change_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_last_state_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateLastStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_name_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateNameErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_non_field_errors_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_platform_service_error_component import (
        ApiV1BlockRolloutItemsArchiveCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_provider_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateProviderErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_provider_id_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_provider_reference_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_reason_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_reconciliation_enabled_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_reconciliation_running_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_reconciliation_task_id_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_reconciliation_task_meta_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_repair_running_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateRepairRunningErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_repair_task_id_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_repair_task_meta_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_rollout_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateRolloutErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_scope_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateScopeErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_sla_availability_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_sla_target_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_slo_availability_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_slo_target_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_source_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateSourceErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_source_user_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateSourceUserErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_state_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateStateErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_state_reason_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateStateReasonErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_status_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateStatusErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_target_availability_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_block_rollout_items_archive_create_tolerations_error_component import (
        ApiV1BlockRolloutItemsArchiveCreateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1BlockRolloutItemsArchiveCreateValidationError")


@_attrs_define
class ApiV1BlockRolloutItemsArchiveCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1BlockRolloutItemsArchiveCreateActionNameErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateActionRunErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateActualAvailabilityErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateAnnotationsErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateArchivedAtErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateArchivedErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateArchivedReasonErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateBlockErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateConditionsErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateCriticalityErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateDebugModeErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateDiscoveryEnabledErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateDiscoveryRunningErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskIdErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskMetaErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateDisplayNameErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateKindErrorComponent | ApiV1BlockRolloutItemsArchiveCreateLabelsErrorComponent
            | ApiV1BlockRolloutItemsArchiveCreateLastStateChangeErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateLastStateErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateNameErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateNonFieldErrorsErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreatePlatformServiceErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateProviderErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateProviderIdErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateProviderReferenceErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateReasonErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateReconciliationEnabledErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateReconciliationRunningErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskIdErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskMetaErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateRepairRunningErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateRepairTaskIdErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateRepairTaskMetaErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateRolloutErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateScopeErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateSlaAvailabilityErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateSlaTargetErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateSloAvailabilityErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateSloTargetErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateSourceErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateSourceUserErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateStateErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateStateReasonErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateStatusErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateTargetAvailabilityErrorComponent |
            ApiV1BlockRolloutItemsArchiveCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1BlockRolloutItemsArchiveCreateActionNameErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateActionRunErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateActualAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateAnnotationsErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateArchivedAtErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateArchivedErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateArchivedReasonErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateBlockErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateConditionsErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateCriticalityErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateDebugModeErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateDiscoveryEnabledErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateDiscoveryRunningErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskIdErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskMetaErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateDisplayNameErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateKindErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateLabelsErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateLastStateChangeErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateLastStateErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateNameErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateNonFieldErrorsErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreatePlatformServiceErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateProviderErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateProviderIdErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateProviderReferenceErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateReasonErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateReconciliationEnabledErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateReconciliationRunningErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskIdErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskMetaErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateRepairRunningErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateRepairTaskIdErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateRepairTaskMetaErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateRolloutErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateScopeErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateSlaAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateSlaTargetErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateSloAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateSloTargetErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateSourceErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateSourceUserErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateStateErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateStateReasonErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateStatusErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateTargetAvailabilityErrorComponent
        | ApiV1BlockRolloutItemsArchiveCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_block_rollout_items_archive_create_action_name_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateActionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_action_run_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateActionRunErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_actual_availability_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_annotations_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_archived_at_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_archived_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_archived_reason_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_block_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_conditions_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_criticality_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_debug_mode_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_discovery_enabled_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_discovery_running_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_discovery_task_id_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_discovery_task_meta_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_display_name_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_kind_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_labels_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_last_state_change_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_last_state_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_name_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_non_field_errors_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_platform_service_error_component import (
            ApiV1BlockRolloutItemsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_provider_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_provider_id_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_provider_reference_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_reconciliation_running_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_repair_running_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_repair_task_id_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_repair_task_meta_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_rollout_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_scope_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_sla_availability_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_sla_target_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_slo_availability_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_slo_target_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_source_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_source_user_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateSourceUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_state_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_state_reason_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_status_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_target_availability_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_tolerations_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateBlockErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateActionNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateStatusErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateSourceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateSourceUserErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateRolloutErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1BlockRolloutItemsArchiveCreateActionRunErrorComponent):
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
        from ..models.api_v1_block_rollout_items_archive_create_action_name_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateActionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_action_run_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateActionRunErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_actual_availability_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_annotations_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_archived_at_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_archived_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_archived_reason_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_block_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateBlockErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_conditions_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_criticality_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_debug_mode_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_discovery_enabled_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_discovery_running_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_discovery_task_id_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_discovery_task_meta_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_display_name_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_kind_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_labels_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_last_state_change_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_last_state_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_name_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_non_field_errors_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_platform_service_error_component import (
            ApiV1BlockRolloutItemsArchiveCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_provider_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_provider_id_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_provider_reference_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_reason_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_reconciliation_enabled_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_reconciliation_running_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_reconciliation_task_id_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_reconciliation_task_meta_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_repair_running_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_repair_task_id_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_repair_task_meta_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_rollout_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateRolloutErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_scope_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_sla_availability_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_sla_target_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_slo_availability_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_slo_target_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_source_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateSourceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_source_user_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateSourceUserErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_state_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_state_reason_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_status_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateStatusErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_target_availability_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_block_rollout_items_archive_create_tolerations_error_component import (
            ApiV1BlockRolloutItemsArchiveCreateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1BlockRolloutItemsArchiveCreateActionNameErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateActionRunErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateActualAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateAnnotationsErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateArchivedAtErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateArchivedErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateArchivedReasonErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateBlockErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateConditionsErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateCriticalityErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateDebugModeErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateDiscoveryEnabledErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateDiscoveryRunningErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskIdErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskMetaErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateDisplayNameErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateKindErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateLabelsErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateLastStateChangeErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateLastStateErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateNameErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateNonFieldErrorsErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreatePlatformServiceErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateProviderErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateProviderIdErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateProviderReferenceErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateReasonErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateReconciliationEnabledErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateReconciliationRunningErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskIdErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskMetaErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateRepairRunningErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateRepairTaskIdErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateRepairTaskMetaErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateRolloutErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateScopeErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateSlaAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateSlaTargetErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateSloAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateSloTargetErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateSourceErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateSourceUserErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateStateErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateStateReasonErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateStatusErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateTargetAvailabilityErrorComponent
                | ApiV1BlockRolloutItemsArchiveCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_0 = (
                        ApiV1BlockRolloutItemsArchiveCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_1 = (
                        ApiV1BlockRolloutItemsArchiveCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_2 = (
                        ApiV1BlockRolloutItemsArchiveCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_3 = (
                        ApiV1BlockRolloutItemsArchiveCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_4 = (
                        ApiV1BlockRolloutItemsArchiveCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_5 = (
                        ApiV1BlockRolloutItemsArchiveCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_6 = (
                        ApiV1BlockRolloutItemsArchiveCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_7 = (
                        ApiV1BlockRolloutItemsArchiveCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_8 = (
                        ApiV1BlockRolloutItemsArchiveCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_9 = (
                        ApiV1BlockRolloutItemsArchiveCreateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_10 = (
                        ApiV1BlockRolloutItemsArchiveCreateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_11 = (
                        ApiV1BlockRolloutItemsArchiveCreateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_12 = (
                        ApiV1BlockRolloutItemsArchiveCreateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_13 = (
                        ApiV1BlockRolloutItemsArchiveCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_14 = (
                        ApiV1BlockRolloutItemsArchiveCreateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_15 = (
                        ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_16 = (
                        ApiV1BlockRolloutItemsArchiveCreateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_17 = (
                        ApiV1BlockRolloutItemsArchiveCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_18 = (
                        ApiV1BlockRolloutItemsArchiveCreateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_19 = (
                        ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_20 = (
                        ApiV1BlockRolloutItemsArchiveCreateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_21 = (
                        ApiV1BlockRolloutItemsArchiveCreateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_22 = (
                        ApiV1BlockRolloutItemsArchiveCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_23 = (
                        ApiV1BlockRolloutItemsArchiveCreateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_24 = (
                        ApiV1BlockRolloutItemsArchiveCreateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_25 = (
                        ApiV1BlockRolloutItemsArchiveCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_26 = (
                        ApiV1BlockRolloutItemsArchiveCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_27 = (
                        ApiV1BlockRolloutItemsArchiveCreateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_28 = (
                        ApiV1BlockRolloutItemsArchiveCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_29 = (
                        ApiV1BlockRolloutItemsArchiveCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_30 = (
                        ApiV1BlockRolloutItemsArchiveCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_31 = (
                        ApiV1BlockRolloutItemsArchiveCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_32 = (
                        ApiV1BlockRolloutItemsArchiveCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_33 = (
                        ApiV1BlockRolloutItemsArchiveCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_34 = (
                        ApiV1BlockRolloutItemsArchiveCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_35 = (
                        ApiV1BlockRolloutItemsArchiveCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_36 = (
                        ApiV1BlockRolloutItemsArchiveCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_37 = (
                        ApiV1BlockRolloutItemsArchiveCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_38 = (
                        ApiV1BlockRolloutItemsArchiveCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_39 = (
                        ApiV1BlockRolloutItemsArchiveCreateBlockErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_40 = (
                        ApiV1BlockRolloutItemsArchiveCreateActionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_41 = (
                        ApiV1BlockRolloutItemsArchiveCreateStatusErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_41
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_42 = (
                        ApiV1BlockRolloutItemsArchiveCreateSourceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_42
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_43 = (
                        ApiV1BlockRolloutItemsArchiveCreateSourceUserErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_43
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_44 = (
                        ApiV1BlockRolloutItemsArchiveCreateRolloutErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_44
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_block_rollout_items_archive_create_error_type_45 = (
                        ApiV1BlockRolloutItemsArchiveCreateActionRunErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_45
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_block_rollout_items_archive_create_error_type_46 = (
                    ApiV1BlockRolloutItemsArchiveCreateReasonErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_block_rollout_items_archive_create_error_type_46

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_block_rollout_items_archive_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_block_rollout_items_archive_create_validation_error.additional_properties = d
        return api_v1_block_rollout_items_archive_create_validation_error

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
