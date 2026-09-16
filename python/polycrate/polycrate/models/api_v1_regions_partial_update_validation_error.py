from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_regions_partial_update_actual_availability_error_component import (
        ApiV1RegionsPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_annotations_error_component import (
        ApiV1RegionsPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_archived_at_error_component import (
        ApiV1RegionsPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_archived_error_component import (
        ApiV1RegionsPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_archived_reason_error_component import (
        ApiV1RegionsPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_conditions_error_component import (
        ApiV1RegionsPartialUpdateConditionsErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_config_error_component import (
        ApiV1RegionsPartialUpdateConfigErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_criticality_error_component import (
        ApiV1RegionsPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_debug_mode_error_component import (
        ApiV1RegionsPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_discovery_enabled_error_component import (
        ApiV1RegionsPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_discovery_running_error_component import (
        ApiV1RegionsPartialUpdateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_discovery_task_id_error_component import (
        ApiV1RegionsPartialUpdateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_discovery_task_meta_error_component import (
        ApiV1RegionsPartialUpdateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_display_name_error_component import (
        ApiV1RegionsPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_kind_error_component import ApiV1RegionsPartialUpdateKindErrorComponent
    from ..models.api_v1_regions_partial_update_labels_error_component import (
        ApiV1RegionsPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_last_state_change_error_component import (
        ApiV1RegionsPartialUpdateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_last_state_error_component import (
        ApiV1RegionsPartialUpdateLastStateErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_name_error_component import ApiV1RegionsPartialUpdateNameErrorComponent
    from ..models.api_v1_regions_partial_update_non_field_errors_error_component import (
        ApiV1RegionsPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_platform_features_error_component import (
        ApiV1RegionsPartialUpdatePlatformFeaturesErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_platform_features_index_error_component import (
        ApiV1RegionsPartialUpdatePlatformFeaturesINDEXErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_platform_service_error_component import (
        ApiV1RegionsPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_provider_error_component import (
        ApiV1RegionsPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_provider_id_error_component import (
        ApiV1RegionsPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_provider_reference_error_component import (
        ApiV1RegionsPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_reconciliation_enabled_error_component import (
        ApiV1RegionsPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_reconciliation_running_error_component import (
        ApiV1RegionsPartialUpdateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_reconciliation_task_id_error_component import (
        ApiV1RegionsPartialUpdateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_reconciliation_task_meta_error_component import (
        ApiV1RegionsPartialUpdateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_repair_running_error_component import (
        ApiV1RegionsPartialUpdateRepairRunningErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_repair_task_id_error_component import (
        ApiV1RegionsPartialUpdateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_repair_task_meta_error_component import (
        ApiV1RegionsPartialUpdateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_scope_error_component import (
        ApiV1RegionsPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_sla_availability_error_component import (
        ApiV1RegionsPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_sla_target_error_component import (
        ApiV1RegionsPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_slo_availability_error_component import (
        ApiV1RegionsPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_slo_target_error_component import (
        ApiV1RegionsPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_state_error_component import (
        ApiV1RegionsPartialUpdateStateErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_state_reason_error_component import (
        ApiV1RegionsPartialUpdateStateReasonErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_target_availability_error_component import (
        ApiV1RegionsPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_partial_update_tolerations_error_component import (
        ApiV1RegionsPartialUpdateTolerationsErrorComponent,
    )


T = TypeVar("T", bound="ApiV1RegionsPartialUpdateValidationError")


@_attrs_define
class ApiV1RegionsPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1RegionsPartialUpdateActualAvailabilityErrorComponent |
            ApiV1RegionsPartialUpdateAnnotationsErrorComponent | ApiV1RegionsPartialUpdateArchivedAtErrorComponent |
            ApiV1RegionsPartialUpdateArchivedErrorComponent | ApiV1RegionsPartialUpdateArchivedReasonErrorComponent |
            ApiV1RegionsPartialUpdateConditionsErrorComponent | ApiV1RegionsPartialUpdateConfigErrorComponent |
            ApiV1RegionsPartialUpdateCriticalityErrorComponent | ApiV1RegionsPartialUpdateDebugModeErrorComponent |
            ApiV1RegionsPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1RegionsPartialUpdateDiscoveryRunningErrorComponent | ApiV1RegionsPartialUpdateDiscoveryTaskIdErrorComponent
            | ApiV1RegionsPartialUpdateDiscoveryTaskMetaErrorComponent | ApiV1RegionsPartialUpdateDisplayNameErrorComponent
            | ApiV1RegionsPartialUpdateKindErrorComponent | ApiV1RegionsPartialUpdateLabelsErrorComponent |
            ApiV1RegionsPartialUpdateLastStateChangeErrorComponent | ApiV1RegionsPartialUpdateLastStateErrorComponent |
            ApiV1RegionsPartialUpdateNameErrorComponent | ApiV1RegionsPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1RegionsPartialUpdatePlatformFeaturesErrorComponent |
            ApiV1RegionsPartialUpdatePlatformFeaturesINDEXErrorComponent |
            ApiV1RegionsPartialUpdatePlatformServiceErrorComponent | ApiV1RegionsPartialUpdateProviderErrorComponent |
            ApiV1RegionsPartialUpdateProviderIdErrorComponent | ApiV1RegionsPartialUpdateProviderReferenceErrorComponent |
            ApiV1RegionsPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1RegionsPartialUpdateReconciliationRunningErrorComponent |
            ApiV1RegionsPartialUpdateReconciliationTaskIdErrorComponent |
            ApiV1RegionsPartialUpdateReconciliationTaskMetaErrorComponent |
            ApiV1RegionsPartialUpdateRepairRunningErrorComponent | ApiV1RegionsPartialUpdateRepairTaskIdErrorComponent |
            ApiV1RegionsPartialUpdateRepairTaskMetaErrorComponent | ApiV1RegionsPartialUpdateScopeErrorComponent |
            ApiV1RegionsPartialUpdateSlaAvailabilityErrorComponent | ApiV1RegionsPartialUpdateSlaTargetErrorComponent |
            ApiV1RegionsPartialUpdateSloAvailabilityErrorComponent | ApiV1RegionsPartialUpdateSloTargetErrorComponent |
            ApiV1RegionsPartialUpdateStateErrorComponent | ApiV1RegionsPartialUpdateStateReasonErrorComponent |
            ApiV1RegionsPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1RegionsPartialUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1RegionsPartialUpdateActualAvailabilityErrorComponent
        | ApiV1RegionsPartialUpdateAnnotationsErrorComponent
        | ApiV1RegionsPartialUpdateArchivedAtErrorComponent
        | ApiV1RegionsPartialUpdateArchivedErrorComponent
        | ApiV1RegionsPartialUpdateArchivedReasonErrorComponent
        | ApiV1RegionsPartialUpdateConditionsErrorComponent
        | ApiV1RegionsPartialUpdateConfigErrorComponent
        | ApiV1RegionsPartialUpdateCriticalityErrorComponent
        | ApiV1RegionsPartialUpdateDebugModeErrorComponent
        | ApiV1RegionsPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1RegionsPartialUpdateDiscoveryRunningErrorComponent
        | ApiV1RegionsPartialUpdateDiscoveryTaskIdErrorComponent
        | ApiV1RegionsPartialUpdateDiscoveryTaskMetaErrorComponent
        | ApiV1RegionsPartialUpdateDisplayNameErrorComponent
        | ApiV1RegionsPartialUpdateKindErrorComponent
        | ApiV1RegionsPartialUpdateLabelsErrorComponent
        | ApiV1RegionsPartialUpdateLastStateChangeErrorComponent
        | ApiV1RegionsPartialUpdateLastStateErrorComponent
        | ApiV1RegionsPartialUpdateNameErrorComponent
        | ApiV1RegionsPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1RegionsPartialUpdatePlatformFeaturesErrorComponent
        | ApiV1RegionsPartialUpdatePlatformFeaturesINDEXErrorComponent
        | ApiV1RegionsPartialUpdatePlatformServiceErrorComponent
        | ApiV1RegionsPartialUpdateProviderErrorComponent
        | ApiV1RegionsPartialUpdateProviderIdErrorComponent
        | ApiV1RegionsPartialUpdateProviderReferenceErrorComponent
        | ApiV1RegionsPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1RegionsPartialUpdateReconciliationRunningErrorComponent
        | ApiV1RegionsPartialUpdateReconciliationTaskIdErrorComponent
        | ApiV1RegionsPartialUpdateReconciliationTaskMetaErrorComponent
        | ApiV1RegionsPartialUpdateRepairRunningErrorComponent
        | ApiV1RegionsPartialUpdateRepairTaskIdErrorComponent
        | ApiV1RegionsPartialUpdateRepairTaskMetaErrorComponent
        | ApiV1RegionsPartialUpdateScopeErrorComponent
        | ApiV1RegionsPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1RegionsPartialUpdateSlaTargetErrorComponent
        | ApiV1RegionsPartialUpdateSloAvailabilityErrorComponent
        | ApiV1RegionsPartialUpdateSloTargetErrorComponent
        | ApiV1RegionsPartialUpdateStateErrorComponent
        | ApiV1RegionsPartialUpdateStateReasonErrorComponent
        | ApiV1RegionsPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1RegionsPartialUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_regions_partial_update_actual_availability_error_component import (
            ApiV1RegionsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_annotations_error_component import (
            ApiV1RegionsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_archived_at_error_component import (
            ApiV1RegionsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_archived_error_component import (
            ApiV1RegionsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_archived_reason_error_component import (
            ApiV1RegionsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_conditions_error_component import (
            ApiV1RegionsPartialUpdateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_criticality_error_component import (
            ApiV1RegionsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_debug_mode_error_component import (
            ApiV1RegionsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_discovery_enabled_error_component import (
            ApiV1RegionsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_discovery_running_error_component import (
            ApiV1RegionsPartialUpdateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_discovery_task_id_error_component import (
            ApiV1RegionsPartialUpdateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_discovery_task_meta_error_component import (
            ApiV1RegionsPartialUpdateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_display_name_error_component import (
            ApiV1RegionsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_kind_error_component import (
            ApiV1RegionsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_labels_error_component import (
            ApiV1RegionsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_last_state_change_error_component import (
            ApiV1RegionsPartialUpdateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_last_state_error_component import (
            ApiV1RegionsPartialUpdateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_name_error_component import (
            ApiV1RegionsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_non_field_errors_error_component import (
            ApiV1RegionsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_platform_features_error_component import (
            ApiV1RegionsPartialUpdatePlatformFeaturesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_platform_features_index_error_component import (
            ApiV1RegionsPartialUpdatePlatformFeaturesINDEXErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_platform_service_error_component import (
            ApiV1RegionsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_provider_error_component import (
            ApiV1RegionsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_provider_id_error_component import (
            ApiV1RegionsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_provider_reference_error_component import (
            ApiV1RegionsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_reconciliation_enabled_error_component import (
            ApiV1RegionsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_reconciliation_running_error_component import (
            ApiV1RegionsPartialUpdateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_reconciliation_task_id_error_component import (
            ApiV1RegionsPartialUpdateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_reconciliation_task_meta_error_component import (
            ApiV1RegionsPartialUpdateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_repair_running_error_component import (
            ApiV1RegionsPartialUpdateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_repair_task_id_error_component import (
            ApiV1RegionsPartialUpdateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_repair_task_meta_error_component import (
            ApiV1RegionsPartialUpdateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_scope_error_component import (
            ApiV1RegionsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_sla_availability_error_component import (
            ApiV1RegionsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_sla_target_error_component import (
            ApiV1RegionsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_slo_availability_error_component import (
            ApiV1RegionsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_slo_target_error_component import (
            ApiV1RegionsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_state_error_component import (
            ApiV1RegionsPartialUpdateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_state_reason_error_component import (
            ApiV1RegionsPartialUpdateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_target_availability_error_component import (
            ApiV1RegionsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_tolerations_error_component import (
            ApiV1RegionsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1RegionsPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateReconciliationTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdatePlatformFeaturesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsPartialUpdatePlatformFeaturesINDEXErrorComponent):
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
        from ..models.api_v1_regions_partial_update_actual_availability_error_component import (
            ApiV1RegionsPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_annotations_error_component import (
            ApiV1RegionsPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_archived_at_error_component import (
            ApiV1RegionsPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_archived_error_component import (
            ApiV1RegionsPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_archived_reason_error_component import (
            ApiV1RegionsPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_conditions_error_component import (
            ApiV1RegionsPartialUpdateConditionsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_config_error_component import (
            ApiV1RegionsPartialUpdateConfigErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_criticality_error_component import (
            ApiV1RegionsPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_debug_mode_error_component import (
            ApiV1RegionsPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_discovery_enabled_error_component import (
            ApiV1RegionsPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_discovery_running_error_component import (
            ApiV1RegionsPartialUpdateDiscoveryRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_discovery_task_id_error_component import (
            ApiV1RegionsPartialUpdateDiscoveryTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_discovery_task_meta_error_component import (
            ApiV1RegionsPartialUpdateDiscoveryTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_display_name_error_component import (
            ApiV1RegionsPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_kind_error_component import (
            ApiV1RegionsPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_labels_error_component import (
            ApiV1RegionsPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_last_state_change_error_component import (
            ApiV1RegionsPartialUpdateLastStateChangeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_last_state_error_component import (
            ApiV1RegionsPartialUpdateLastStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_name_error_component import (
            ApiV1RegionsPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_non_field_errors_error_component import (
            ApiV1RegionsPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_platform_features_error_component import (
            ApiV1RegionsPartialUpdatePlatformFeaturesErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_platform_features_index_error_component import (
            ApiV1RegionsPartialUpdatePlatformFeaturesINDEXErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_platform_service_error_component import (
            ApiV1RegionsPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_provider_error_component import (
            ApiV1RegionsPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_provider_id_error_component import (
            ApiV1RegionsPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_provider_reference_error_component import (
            ApiV1RegionsPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_reconciliation_enabled_error_component import (
            ApiV1RegionsPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_reconciliation_running_error_component import (
            ApiV1RegionsPartialUpdateReconciliationRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_reconciliation_task_id_error_component import (
            ApiV1RegionsPartialUpdateReconciliationTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_reconciliation_task_meta_error_component import (
            ApiV1RegionsPartialUpdateReconciliationTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_repair_running_error_component import (
            ApiV1RegionsPartialUpdateRepairRunningErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_repair_task_id_error_component import (
            ApiV1RegionsPartialUpdateRepairTaskIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_repair_task_meta_error_component import (
            ApiV1RegionsPartialUpdateRepairTaskMetaErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_scope_error_component import (
            ApiV1RegionsPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_sla_availability_error_component import (
            ApiV1RegionsPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_sla_target_error_component import (
            ApiV1RegionsPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_slo_availability_error_component import (
            ApiV1RegionsPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_slo_target_error_component import (
            ApiV1RegionsPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_state_error_component import (
            ApiV1RegionsPartialUpdateStateErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_state_reason_error_component import (
            ApiV1RegionsPartialUpdateStateReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_target_availability_error_component import (
            ApiV1RegionsPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_regions_partial_update_tolerations_error_component import (
            ApiV1RegionsPartialUpdateTolerationsErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1RegionsPartialUpdateActualAvailabilityErrorComponent
                | ApiV1RegionsPartialUpdateAnnotationsErrorComponent
                | ApiV1RegionsPartialUpdateArchivedAtErrorComponent
                | ApiV1RegionsPartialUpdateArchivedErrorComponent
                | ApiV1RegionsPartialUpdateArchivedReasonErrorComponent
                | ApiV1RegionsPartialUpdateConditionsErrorComponent
                | ApiV1RegionsPartialUpdateConfigErrorComponent
                | ApiV1RegionsPartialUpdateCriticalityErrorComponent
                | ApiV1RegionsPartialUpdateDebugModeErrorComponent
                | ApiV1RegionsPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1RegionsPartialUpdateDiscoveryRunningErrorComponent
                | ApiV1RegionsPartialUpdateDiscoveryTaskIdErrorComponent
                | ApiV1RegionsPartialUpdateDiscoveryTaskMetaErrorComponent
                | ApiV1RegionsPartialUpdateDisplayNameErrorComponent
                | ApiV1RegionsPartialUpdateKindErrorComponent
                | ApiV1RegionsPartialUpdateLabelsErrorComponent
                | ApiV1RegionsPartialUpdateLastStateChangeErrorComponent
                | ApiV1RegionsPartialUpdateLastStateErrorComponent
                | ApiV1RegionsPartialUpdateNameErrorComponent
                | ApiV1RegionsPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1RegionsPartialUpdatePlatformFeaturesErrorComponent
                | ApiV1RegionsPartialUpdatePlatformFeaturesINDEXErrorComponent
                | ApiV1RegionsPartialUpdatePlatformServiceErrorComponent
                | ApiV1RegionsPartialUpdateProviderErrorComponent
                | ApiV1RegionsPartialUpdateProviderIdErrorComponent
                | ApiV1RegionsPartialUpdateProviderReferenceErrorComponent
                | ApiV1RegionsPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1RegionsPartialUpdateReconciliationRunningErrorComponent
                | ApiV1RegionsPartialUpdateReconciliationTaskIdErrorComponent
                | ApiV1RegionsPartialUpdateReconciliationTaskMetaErrorComponent
                | ApiV1RegionsPartialUpdateRepairRunningErrorComponent
                | ApiV1RegionsPartialUpdateRepairTaskIdErrorComponent
                | ApiV1RegionsPartialUpdateRepairTaskMetaErrorComponent
                | ApiV1RegionsPartialUpdateScopeErrorComponent
                | ApiV1RegionsPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1RegionsPartialUpdateSlaTargetErrorComponent
                | ApiV1RegionsPartialUpdateSloAvailabilityErrorComponent
                | ApiV1RegionsPartialUpdateSloTargetErrorComponent
                | ApiV1RegionsPartialUpdateStateErrorComponent
                | ApiV1RegionsPartialUpdateStateReasonErrorComponent
                | ApiV1RegionsPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1RegionsPartialUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_0 = (
                        ApiV1RegionsPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_1 = (
                        ApiV1RegionsPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_2 = (
                        ApiV1RegionsPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_3 = (
                        ApiV1RegionsPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_4 = (
                        ApiV1RegionsPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_5 = (
                        ApiV1RegionsPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_6 = (
                        ApiV1RegionsPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_7 = (
                        ApiV1RegionsPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_8 = (
                        ApiV1RegionsPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_9 = (
                        ApiV1RegionsPartialUpdateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_10 = (
                        ApiV1RegionsPartialUpdateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_11 = (
                        ApiV1RegionsPartialUpdateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_12 = (
                        ApiV1RegionsPartialUpdateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_13 = (
                        ApiV1RegionsPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_14 = (
                        ApiV1RegionsPartialUpdateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_15 = (
                        ApiV1RegionsPartialUpdateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_16 = (
                        ApiV1RegionsPartialUpdateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_17 = (
                        ApiV1RegionsPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_18 = (
                        ApiV1RegionsPartialUpdateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_19 = (
                        ApiV1RegionsPartialUpdateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_20 = (
                        ApiV1RegionsPartialUpdateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_21 = (
                        ApiV1RegionsPartialUpdateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_22 = (
                        ApiV1RegionsPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_23 = (
                        ApiV1RegionsPartialUpdateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_24 = (
                        ApiV1RegionsPartialUpdateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_25 = (
                        ApiV1RegionsPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_26 = (
                        ApiV1RegionsPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_27 = (
                        ApiV1RegionsPartialUpdateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_28 = (
                        ApiV1RegionsPartialUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_29 = (
                        ApiV1RegionsPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_30 = (
                        ApiV1RegionsPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_31 = (
                        ApiV1RegionsPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_32 = (
                        ApiV1RegionsPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_33 = (
                        ApiV1RegionsPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_34 = (
                        ApiV1RegionsPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_35 = (
                        ApiV1RegionsPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_36 = (
                        ApiV1RegionsPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_37 = (
                        ApiV1RegionsPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_38 = (
                        ApiV1RegionsPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_39 = (
                        ApiV1RegionsPartialUpdatePlatformFeaturesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_partial_update_error_type_40 = (
                        ApiV1RegionsPartialUpdatePlatformFeaturesINDEXErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_partial_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_regions_partial_update_error_type_41 = (
                    ApiV1RegionsPartialUpdateConfigErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_regions_partial_update_error_type_41

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_regions_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_regions_partial_update_validation_error.additional_properties = d
        return api_v1_regions_partial_update_validation_error

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
