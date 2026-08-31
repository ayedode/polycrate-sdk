from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_regions_update_actual_availability_error_component import (
        ApiV1RegionsUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_update_annotations_error_component import ApiV1RegionsUpdateAnnotationsErrorComponent
    from ..models.api_v1_regions_update_archived_at_error_component import ApiV1RegionsUpdateArchivedAtErrorComponent
    from ..models.api_v1_regions_update_archived_error_component import ApiV1RegionsUpdateArchivedErrorComponent
    from ..models.api_v1_regions_update_archived_reason_error_component import (
        ApiV1RegionsUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_regions_update_conditions_error_component import ApiV1RegionsUpdateConditionsErrorComponent
    from ..models.api_v1_regions_update_config_error_component import ApiV1RegionsUpdateConfigErrorComponent
    from ..models.api_v1_regions_update_criticality_error_component import ApiV1RegionsUpdateCriticalityErrorComponent
    from ..models.api_v1_regions_update_debug_mode_error_component import ApiV1RegionsUpdateDebugModeErrorComponent
    from ..models.api_v1_regions_update_discovery_enabled_error_component import (
        ApiV1RegionsUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_regions_update_discovery_running_error_component import (
        ApiV1RegionsUpdateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_regions_update_discovery_task_id_error_component import (
        ApiV1RegionsUpdateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_regions_update_discovery_task_meta_error_component import (
        ApiV1RegionsUpdateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_regions_update_display_name_error_component import ApiV1RegionsUpdateDisplayNameErrorComponent
    from ..models.api_v1_regions_update_kind_error_component import ApiV1RegionsUpdateKindErrorComponent
    from ..models.api_v1_regions_update_labels_error_component import ApiV1RegionsUpdateLabelsErrorComponent
    from ..models.api_v1_regions_update_last_state_change_error_component import (
        ApiV1RegionsUpdateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_regions_update_last_state_error_component import ApiV1RegionsUpdateLastStateErrorComponent
    from ..models.api_v1_regions_update_name_error_component import ApiV1RegionsUpdateNameErrorComponent
    from ..models.api_v1_regions_update_non_field_errors_error_component import (
        ApiV1RegionsUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_regions_update_platform_features_error_component import (
        ApiV1RegionsUpdatePlatformFeaturesErrorComponent,
    )
    from ..models.api_v1_regions_update_platform_features_index_error_component import (
        ApiV1RegionsUpdatePlatformFeaturesINDEXErrorComponent,
    )
    from ..models.api_v1_regions_update_platform_service_error_component import (
        ApiV1RegionsUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_regions_update_provider_error_component import ApiV1RegionsUpdateProviderErrorComponent
    from ..models.api_v1_regions_update_provider_id_error_component import ApiV1RegionsUpdateProviderIdErrorComponent
    from ..models.api_v1_regions_update_provider_reference_error_component import (
        ApiV1RegionsUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_regions_update_reconciliation_enabled_error_component import (
        ApiV1RegionsUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_regions_update_reconciliation_running_error_component import (
        ApiV1RegionsUpdateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_regions_update_reconciliation_task_id_error_component import (
        ApiV1RegionsUpdateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_regions_update_reconciliation_task_meta_error_component import (
        ApiV1RegionsUpdateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_regions_update_repair_running_error_component import (
        ApiV1RegionsUpdateRepairRunningErrorComponent,
    )
    from ..models.api_v1_regions_update_repair_task_id_error_component import (
        ApiV1RegionsUpdateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_regions_update_repair_task_meta_error_component import (
        ApiV1RegionsUpdateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_regions_update_scope_error_component import ApiV1RegionsUpdateScopeErrorComponent
    from ..models.api_v1_regions_update_sla_availability_error_component import (
        ApiV1RegionsUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_update_sla_target_error_component import ApiV1RegionsUpdateSlaTargetErrorComponent
    from ..models.api_v1_regions_update_slo_availability_error_component import (
        ApiV1RegionsUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_update_slo_target_error_component import ApiV1RegionsUpdateSloTargetErrorComponent
    from ..models.api_v1_regions_update_state_error_component import ApiV1RegionsUpdateStateErrorComponent
    from ..models.api_v1_regions_update_state_reason_error_component import ApiV1RegionsUpdateStateReasonErrorComponent
    from ..models.api_v1_regions_update_target_availability_error_component import (
        ApiV1RegionsUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_update_tolerations_error_component import ApiV1RegionsUpdateTolerationsErrorComponent


T = TypeVar("T", bound="ApiV1RegionsUpdateValidationError")


@_attrs_define
class ApiV1RegionsUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1RegionsUpdateActualAvailabilityErrorComponent | ApiV1RegionsUpdateAnnotationsErrorComponent |
            ApiV1RegionsUpdateArchivedAtErrorComponent | ApiV1RegionsUpdateArchivedErrorComponent |
            ApiV1RegionsUpdateArchivedReasonErrorComponent | ApiV1RegionsUpdateConditionsErrorComponent |
            ApiV1RegionsUpdateConfigErrorComponent | ApiV1RegionsUpdateCriticalityErrorComponent |
            ApiV1RegionsUpdateDebugModeErrorComponent | ApiV1RegionsUpdateDiscoveryEnabledErrorComponent |
            ApiV1RegionsUpdateDiscoveryRunningErrorComponent | ApiV1RegionsUpdateDiscoveryTaskIdErrorComponent |
            ApiV1RegionsUpdateDiscoveryTaskMetaErrorComponent | ApiV1RegionsUpdateDisplayNameErrorComponent |
            ApiV1RegionsUpdateKindErrorComponent | ApiV1RegionsUpdateLabelsErrorComponent |
            ApiV1RegionsUpdateLastStateChangeErrorComponent | ApiV1RegionsUpdateLastStateErrorComponent |
            ApiV1RegionsUpdateNameErrorComponent | ApiV1RegionsUpdateNonFieldErrorsErrorComponent |
            ApiV1RegionsUpdatePlatformFeaturesErrorComponent | ApiV1RegionsUpdatePlatformFeaturesINDEXErrorComponent |
            ApiV1RegionsUpdatePlatformServiceErrorComponent | ApiV1RegionsUpdateProviderErrorComponent |
            ApiV1RegionsUpdateProviderIdErrorComponent | ApiV1RegionsUpdateProviderReferenceErrorComponent |
            ApiV1RegionsUpdateReconciliationEnabledErrorComponent | ApiV1RegionsUpdateReconciliationRunningErrorComponent |
            ApiV1RegionsUpdateReconciliationTaskIdErrorComponent | ApiV1RegionsUpdateReconciliationTaskMetaErrorComponent |
            ApiV1RegionsUpdateRepairRunningErrorComponent | ApiV1RegionsUpdateRepairTaskIdErrorComponent |
            ApiV1RegionsUpdateRepairTaskMetaErrorComponent | ApiV1RegionsUpdateScopeErrorComponent |
            ApiV1RegionsUpdateSlaAvailabilityErrorComponent | ApiV1RegionsUpdateSlaTargetErrorComponent |
            ApiV1RegionsUpdateSloAvailabilityErrorComponent | ApiV1RegionsUpdateSloTargetErrorComponent |
            ApiV1RegionsUpdateStateErrorComponent | ApiV1RegionsUpdateStateReasonErrorComponent |
            ApiV1RegionsUpdateTargetAvailabilityErrorComponent | ApiV1RegionsUpdateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1RegionsUpdateActualAvailabilityErrorComponent
        | ApiV1RegionsUpdateAnnotationsErrorComponent
        | ApiV1RegionsUpdateArchivedAtErrorComponent
        | ApiV1RegionsUpdateArchivedErrorComponent
        | ApiV1RegionsUpdateArchivedReasonErrorComponent
        | ApiV1RegionsUpdateConditionsErrorComponent
        | ApiV1RegionsUpdateConfigErrorComponent
        | ApiV1RegionsUpdateCriticalityErrorComponent
        | ApiV1RegionsUpdateDebugModeErrorComponent
        | ApiV1RegionsUpdateDiscoveryEnabledErrorComponent
        | ApiV1RegionsUpdateDiscoveryRunningErrorComponent
        | ApiV1RegionsUpdateDiscoveryTaskIdErrorComponent
        | ApiV1RegionsUpdateDiscoveryTaskMetaErrorComponent
        | ApiV1RegionsUpdateDisplayNameErrorComponent
        | ApiV1RegionsUpdateKindErrorComponent
        | ApiV1RegionsUpdateLabelsErrorComponent
        | ApiV1RegionsUpdateLastStateChangeErrorComponent
        | ApiV1RegionsUpdateLastStateErrorComponent
        | ApiV1RegionsUpdateNameErrorComponent
        | ApiV1RegionsUpdateNonFieldErrorsErrorComponent
        | ApiV1RegionsUpdatePlatformFeaturesErrorComponent
        | ApiV1RegionsUpdatePlatformFeaturesINDEXErrorComponent
        | ApiV1RegionsUpdatePlatformServiceErrorComponent
        | ApiV1RegionsUpdateProviderErrorComponent
        | ApiV1RegionsUpdateProviderIdErrorComponent
        | ApiV1RegionsUpdateProviderReferenceErrorComponent
        | ApiV1RegionsUpdateReconciliationEnabledErrorComponent
        | ApiV1RegionsUpdateReconciliationRunningErrorComponent
        | ApiV1RegionsUpdateReconciliationTaskIdErrorComponent
        | ApiV1RegionsUpdateReconciliationTaskMetaErrorComponent
        | ApiV1RegionsUpdateRepairRunningErrorComponent
        | ApiV1RegionsUpdateRepairTaskIdErrorComponent
        | ApiV1RegionsUpdateRepairTaskMetaErrorComponent
        | ApiV1RegionsUpdateScopeErrorComponent
        | ApiV1RegionsUpdateSlaAvailabilityErrorComponent
        | ApiV1RegionsUpdateSlaTargetErrorComponent
        | ApiV1RegionsUpdateSloAvailabilityErrorComponent
        | ApiV1RegionsUpdateSloTargetErrorComponent
        | ApiV1RegionsUpdateStateErrorComponent
        | ApiV1RegionsUpdateStateReasonErrorComponent
        | ApiV1RegionsUpdateTargetAvailabilityErrorComponent
        | ApiV1RegionsUpdateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_regions_update_actual_availability_error_component import (
            ApiV1RegionsUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_update_annotations_error_component import (
            ApiV1RegionsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_regions_update_archived_at_error_component import (
            ApiV1RegionsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_regions_update_archived_error_component import ApiV1RegionsUpdateArchivedErrorComponent
        from ..models.api_v1_regions_update_archived_reason_error_component import (
            ApiV1RegionsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_regions_update_conditions_error_component import ApiV1RegionsUpdateConditionsErrorComponent
        from ..models.api_v1_regions_update_criticality_error_component import (
            ApiV1RegionsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_regions_update_debug_mode_error_component import ApiV1RegionsUpdateDebugModeErrorComponent
        from ..models.api_v1_regions_update_discovery_enabled_error_component import (
            ApiV1RegionsUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_regions_update_discovery_running_error_component import (
            ApiV1RegionsUpdateDiscoveryRunningErrorComponent,
        )
        from ..models.api_v1_regions_update_discovery_task_id_error_component import (
            ApiV1RegionsUpdateDiscoveryTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_update_discovery_task_meta_error_component import (
            ApiV1RegionsUpdateDiscoveryTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_update_display_name_error_component import (
            ApiV1RegionsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_regions_update_kind_error_component import ApiV1RegionsUpdateKindErrorComponent
        from ..models.api_v1_regions_update_labels_error_component import ApiV1RegionsUpdateLabelsErrorComponent
        from ..models.api_v1_regions_update_last_state_change_error_component import (
            ApiV1RegionsUpdateLastStateChangeErrorComponent,
        )
        from ..models.api_v1_regions_update_last_state_error_component import ApiV1RegionsUpdateLastStateErrorComponent
        from ..models.api_v1_regions_update_name_error_component import ApiV1RegionsUpdateNameErrorComponent
        from ..models.api_v1_regions_update_non_field_errors_error_component import (
            ApiV1RegionsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_regions_update_platform_features_error_component import (
            ApiV1RegionsUpdatePlatformFeaturesErrorComponent,
        )
        from ..models.api_v1_regions_update_platform_features_index_error_component import (
            ApiV1RegionsUpdatePlatformFeaturesINDEXErrorComponent,
        )
        from ..models.api_v1_regions_update_platform_service_error_component import (
            ApiV1RegionsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_regions_update_provider_error_component import ApiV1RegionsUpdateProviderErrorComponent
        from ..models.api_v1_regions_update_provider_id_error_component import (
            ApiV1RegionsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_regions_update_provider_reference_error_component import (
            ApiV1RegionsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_regions_update_reconciliation_enabled_error_component import (
            ApiV1RegionsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_regions_update_reconciliation_running_error_component import (
            ApiV1RegionsUpdateReconciliationRunningErrorComponent,
        )
        from ..models.api_v1_regions_update_reconciliation_task_id_error_component import (
            ApiV1RegionsUpdateReconciliationTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_update_reconciliation_task_meta_error_component import (
            ApiV1RegionsUpdateReconciliationTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_update_repair_running_error_component import (
            ApiV1RegionsUpdateRepairRunningErrorComponent,
        )
        from ..models.api_v1_regions_update_repair_task_id_error_component import (
            ApiV1RegionsUpdateRepairTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_update_repair_task_meta_error_component import (
            ApiV1RegionsUpdateRepairTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_update_scope_error_component import ApiV1RegionsUpdateScopeErrorComponent
        from ..models.api_v1_regions_update_sla_availability_error_component import (
            ApiV1RegionsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_update_sla_target_error_component import ApiV1RegionsUpdateSlaTargetErrorComponent
        from ..models.api_v1_regions_update_slo_availability_error_component import (
            ApiV1RegionsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_update_slo_target_error_component import ApiV1RegionsUpdateSloTargetErrorComponent
        from ..models.api_v1_regions_update_state_error_component import ApiV1RegionsUpdateStateErrorComponent
        from ..models.api_v1_regions_update_state_reason_error_component import (
            ApiV1RegionsUpdateStateReasonErrorComponent,
        )
        from ..models.api_v1_regions_update_target_availability_error_component import (
            ApiV1RegionsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_update_tolerations_error_component import (
            ApiV1RegionsUpdateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1RegionsUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateReconciliationTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdatePlatformFeaturesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsUpdatePlatformFeaturesINDEXErrorComponent):
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
        from ..models.api_v1_regions_update_actual_availability_error_component import (
            ApiV1RegionsUpdateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_update_annotations_error_component import (
            ApiV1RegionsUpdateAnnotationsErrorComponent,
        )
        from ..models.api_v1_regions_update_archived_at_error_component import (
            ApiV1RegionsUpdateArchivedAtErrorComponent,
        )
        from ..models.api_v1_regions_update_archived_error_component import ApiV1RegionsUpdateArchivedErrorComponent
        from ..models.api_v1_regions_update_archived_reason_error_component import (
            ApiV1RegionsUpdateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_regions_update_conditions_error_component import ApiV1RegionsUpdateConditionsErrorComponent
        from ..models.api_v1_regions_update_config_error_component import ApiV1RegionsUpdateConfigErrorComponent
        from ..models.api_v1_regions_update_criticality_error_component import (
            ApiV1RegionsUpdateCriticalityErrorComponent,
        )
        from ..models.api_v1_regions_update_debug_mode_error_component import ApiV1RegionsUpdateDebugModeErrorComponent
        from ..models.api_v1_regions_update_discovery_enabled_error_component import (
            ApiV1RegionsUpdateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_regions_update_discovery_running_error_component import (
            ApiV1RegionsUpdateDiscoveryRunningErrorComponent,
        )
        from ..models.api_v1_regions_update_discovery_task_id_error_component import (
            ApiV1RegionsUpdateDiscoveryTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_update_discovery_task_meta_error_component import (
            ApiV1RegionsUpdateDiscoveryTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_update_display_name_error_component import (
            ApiV1RegionsUpdateDisplayNameErrorComponent,
        )
        from ..models.api_v1_regions_update_kind_error_component import ApiV1RegionsUpdateKindErrorComponent
        from ..models.api_v1_regions_update_labels_error_component import ApiV1RegionsUpdateLabelsErrorComponent
        from ..models.api_v1_regions_update_last_state_change_error_component import (
            ApiV1RegionsUpdateLastStateChangeErrorComponent,
        )
        from ..models.api_v1_regions_update_last_state_error_component import ApiV1RegionsUpdateLastStateErrorComponent
        from ..models.api_v1_regions_update_name_error_component import ApiV1RegionsUpdateNameErrorComponent
        from ..models.api_v1_regions_update_non_field_errors_error_component import (
            ApiV1RegionsUpdateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_regions_update_platform_features_error_component import (
            ApiV1RegionsUpdatePlatformFeaturesErrorComponent,
        )
        from ..models.api_v1_regions_update_platform_features_index_error_component import (
            ApiV1RegionsUpdatePlatformFeaturesINDEXErrorComponent,
        )
        from ..models.api_v1_regions_update_platform_service_error_component import (
            ApiV1RegionsUpdatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_regions_update_provider_error_component import ApiV1RegionsUpdateProviderErrorComponent
        from ..models.api_v1_regions_update_provider_id_error_component import (
            ApiV1RegionsUpdateProviderIdErrorComponent,
        )
        from ..models.api_v1_regions_update_provider_reference_error_component import (
            ApiV1RegionsUpdateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_regions_update_reconciliation_enabled_error_component import (
            ApiV1RegionsUpdateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_regions_update_reconciliation_running_error_component import (
            ApiV1RegionsUpdateReconciliationRunningErrorComponent,
        )
        from ..models.api_v1_regions_update_reconciliation_task_id_error_component import (
            ApiV1RegionsUpdateReconciliationTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_update_reconciliation_task_meta_error_component import (
            ApiV1RegionsUpdateReconciliationTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_update_repair_running_error_component import (
            ApiV1RegionsUpdateRepairRunningErrorComponent,
        )
        from ..models.api_v1_regions_update_repair_task_id_error_component import (
            ApiV1RegionsUpdateRepairTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_update_repair_task_meta_error_component import (
            ApiV1RegionsUpdateRepairTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_update_scope_error_component import ApiV1RegionsUpdateScopeErrorComponent
        from ..models.api_v1_regions_update_sla_availability_error_component import (
            ApiV1RegionsUpdateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_update_sla_target_error_component import ApiV1RegionsUpdateSlaTargetErrorComponent
        from ..models.api_v1_regions_update_slo_availability_error_component import (
            ApiV1RegionsUpdateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_update_slo_target_error_component import ApiV1RegionsUpdateSloTargetErrorComponent
        from ..models.api_v1_regions_update_state_error_component import ApiV1RegionsUpdateStateErrorComponent
        from ..models.api_v1_regions_update_state_reason_error_component import (
            ApiV1RegionsUpdateStateReasonErrorComponent,
        )
        from ..models.api_v1_regions_update_target_availability_error_component import (
            ApiV1RegionsUpdateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_update_tolerations_error_component import (
            ApiV1RegionsUpdateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1RegionsUpdateActualAvailabilityErrorComponent
                | ApiV1RegionsUpdateAnnotationsErrorComponent
                | ApiV1RegionsUpdateArchivedAtErrorComponent
                | ApiV1RegionsUpdateArchivedErrorComponent
                | ApiV1RegionsUpdateArchivedReasonErrorComponent
                | ApiV1RegionsUpdateConditionsErrorComponent
                | ApiV1RegionsUpdateConfigErrorComponent
                | ApiV1RegionsUpdateCriticalityErrorComponent
                | ApiV1RegionsUpdateDebugModeErrorComponent
                | ApiV1RegionsUpdateDiscoveryEnabledErrorComponent
                | ApiV1RegionsUpdateDiscoveryRunningErrorComponent
                | ApiV1RegionsUpdateDiscoveryTaskIdErrorComponent
                | ApiV1RegionsUpdateDiscoveryTaskMetaErrorComponent
                | ApiV1RegionsUpdateDisplayNameErrorComponent
                | ApiV1RegionsUpdateKindErrorComponent
                | ApiV1RegionsUpdateLabelsErrorComponent
                | ApiV1RegionsUpdateLastStateChangeErrorComponent
                | ApiV1RegionsUpdateLastStateErrorComponent
                | ApiV1RegionsUpdateNameErrorComponent
                | ApiV1RegionsUpdateNonFieldErrorsErrorComponent
                | ApiV1RegionsUpdatePlatformFeaturesErrorComponent
                | ApiV1RegionsUpdatePlatformFeaturesINDEXErrorComponent
                | ApiV1RegionsUpdatePlatformServiceErrorComponent
                | ApiV1RegionsUpdateProviderErrorComponent
                | ApiV1RegionsUpdateProviderIdErrorComponent
                | ApiV1RegionsUpdateProviderReferenceErrorComponent
                | ApiV1RegionsUpdateReconciliationEnabledErrorComponent
                | ApiV1RegionsUpdateReconciliationRunningErrorComponent
                | ApiV1RegionsUpdateReconciliationTaskIdErrorComponent
                | ApiV1RegionsUpdateReconciliationTaskMetaErrorComponent
                | ApiV1RegionsUpdateRepairRunningErrorComponent
                | ApiV1RegionsUpdateRepairTaskIdErrorComponent
                | ApiV1RegionsUpdateRepairTaskMetaErrorComponent
                | ApiV1RegionsUpdateScopeErrorComponent
                | ApiV1RegionsUpdateSlaAvailabilityErrorComponent
                | ApiV1RegionsUpdateSlaTargetErrorComponent
                | ApiV1RegionsUpdateSloAvailabilityErrorComponent
                | ApiV1RegionsUpdateSloTargetErrorComponent
                | ApiV1RegionsUpdateStateErrorComponent
                | ApiV1RegionsUpdateStateReasonErrorComponent
                | ApiV1RegionsUpdateTargetAvailabilityErrorComponent
                | ApiV1RegionsUpdateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_0 = (
                        ApiV1RegionsUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_1 = (
                        ApiV1RegionsUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_2 = (
                        ApiV1RegionsUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_3 = (
                        ApiV1RegionsUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_4 = (
                        ApiV1RegionsUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_5 = (
                        ApiV1RegionsUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_6 = (
                        ApiV1RegionsUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_7 = (
                        ApiV1RegionsUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_8 = (
                        ApiV1RegionsUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_9 = (
                        ApiV1RegionsUpdateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_10 = (
                        ApiV1RegionsUpdateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_11 = (
                        ApiV1RegionsUpdateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_12 = (
                        ApiV1RegionsUpdateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_13 = (
                        ApiV1RegionsUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_14 = (
                        ApiV1RegionsUpdateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_15 = (
                        ApiV1RegionsUpdateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_16 = (
                        ApiV1RegionsUpdateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_17 = (
                        ApiV1RegionsUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_18 = (
                        ApiV1RegionsUpdateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_19 = (
                        ApiV1RegionsUpdateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_20 = (
                        ApiV1RegionsUpdateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_21 = (
                        ApiV1RegionsUpdateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_22 = (
                        ApiV1RegionsUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_23 = (
                        ApiV1RegionsUpdateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_24 = (
                        ApiV1RegionsUpdateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_25 = (
                        ApiV1RegionsUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_26 = (
                        ApiV1RegionsUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_27 = (
                        ApiV1RegionsUpdateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_28 = (
                        ApiV1RegionsUpdateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_29 = (
                        ApiV1RegionsUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_30 = (
                        ApiV1RegionsUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_31 = (
                        ApiV1RegionsUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_32 = (
                        ApiV1RegionsUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_33 = (
                        ApiV1RegionsUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_34 = (
                        ApiV1RegionsUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_35 = (
                        ApiV1RegionsUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_36 = (
                        ApiV1RegionsUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_37 = (
                        ApiV1RegionsUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_38 = (
                        ApiV1RegionsUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_39 = (
                        ApiV1RegionsUpdatePlatformFeaturesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_update_error_type_40 = (
                        ApiV1RegionsUpdatePlatformFeaturesINDEXErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_update_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_regions_update_error_type_41 = (
                    ApiV1RegionsUpdateConfigErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_regions_update_error_type_41

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_regions_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_regions_update_validation_error.additional_properties = d
        return api_v1_regions_update_validation_error

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
