from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_regions_create_actual_availability_error_component import (
        ApiV1RegionsCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_create_annotations_error_component import ApiV1RegionsCreateAnnotationsErrorComponent
    from ..models.api_v1_regions_create_archived_at_error_component import ApiV1RegionsCreateArchivedAtErrorComponent
    from ..models.api_v1_regions_create_archived_error_component import ApiV1RegionsCreateArchivedErrorComponent
    from ..models.api_v1_regions_create_archived_reason_error_component import (
        ApiV1RegionsCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_regions_create_conditions_error_component import ApiV1RegionsCreateConditionsErrorComponent
    from ..models.api_v1_regions_create_config_error_component import ApiV1RegionsCreateConfigErrorComponent
    from ..models.api_v1_regions_create_criticality_error_component import ApiV1RegionsCreateCriticalityErrorComponent
    from ..models.api_v1_regions_create_debug_mode_error_component import ApiV1RegionsCreateDebugModeErrorComponent
    from ..models.api_v1_regions_create_discovery_enabled_error_component import (
        ApiV1RegionsCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_regions_create_discovery_running_error_component import (
        ApiV1RegionsCreateDiscoveryRunningErrorComponent,
    )
    from ..models.api_v1_regions_create_discovery_task_id_error_component import (
        ApiV1RegionsCreateDiscoveryTaskIdErrorComponent,
    )
    from ..models.api_v1_regions_create_discovery_task_meta_error_component import (
        ApiV1RegionsCreateDiscoveryTaskMetaErrorComponent,
    )
    from ..models.api_v1_regions_create_display_name_error_component import ApiV1RegionsCreateDisplayNameErrorComponent
    from ..models.api_v1_regions_create_kind_error_component import ApiV1RegionsCreateKindErrorComponent
    from ..models.api_v1_regions_create_labels_error_component import ApiV1RegionsCreateLabelsErrorComponent
    from ..models.api_v1_regions_create_last_state_change_error_component import (
        ApiV1RegionsCreateLastStateChangeErrorComponent,
    )
    from ..models.api_v1_regions_create_last_state_error_component import ApiV1RegionsCreateLastStateErrorComponent
    from ..models.api_v1_regions_create_name_error_component import ApiV1RegionsCreateNameErrorComponent
    from ..models.api_v1_regions_create_non_field_errors_error_component import (
        ApiV1RegionsCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_regions_create_platform_features_error_component import (
        ApiV1RegionsCreatePlatformFeaturesErrorComponent,
    )
    from ..models.api_v1_regions_create_platform_features_index_error_component import (
        ApiV1RegionsCreatePlatformFeaturesINDEXErrorComponent,
    )
    from ..models.api_v1_regions_create_platform_service_error_component import (
        ApiV1RegionsCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_regions_create_provider_error_component import ApiV1RegionsCreateProviderErrorComponent
    from ..models.api_v1_regions_create_provider_id_error_component import ApiV1RegionsCreateProviderIdErrorComponent
    from ..models.api_v1_regions_create_provider_reference_error_component import (
        ApiV1RegionsCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_regions_create_reconciliation_enabled_error_component import (
        ApiV1RegionsCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_regions_create_reconciliation_running_error_component import (
        ApiV1RegionsCreateReconciliationRunningErrorComponent,
    )
    from ..models.api_v1_regions_create_reconciliation_task_id_error_component import (
        ApiV1RegionsCreateReconciliationTaskIdErrorComponent,
    )
    from ..models.api_v1_regions_create_reconciliation_task_meta_error_component import (
        ApiV1RegionsCreateReconciliationTaskMetaErrorComponent,
    )
    from ..models.api_v1_regions_create_repair_running_error_component import (
        ApiV1RegionsCreateRepairRunningErrorComponent,
    )
    from ..models.api_v1_regions_create_repair_task_id_error_component import (
        ApiV1RegionsCreateRepairTaskIdErrorComponent,
    )
    from ..models.api_v1_regions_create_repair_task_meta_error_component import (
        ApiV1RegionsCreateRepairTaskMetaErrorComponent,
    )
    from ..models.api_v1_regions_create_scope_error_component import ApiV1RegionsCreateScopeErrorComponent
    from ..models.api_v1_regions_create_sla_availability_error_component import (
        ApiV1RegionsCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_create_sla_target_error_component import ApiV1RegionsCreateSlaTargetErrorComponent
    from ..models.api_v1_regions_create_slo_availability_error_component import (
        ApiV1RegionsCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_create_slo_target_error_component import ApiV1RegionsCreateSloTargetErrorComponent
    from ..models.api_v1_regions_create_state_error_component import ApiV1RegionsCreateStateErrorComponent
    from ..models.api_v1_regions_create_state_reason_error_component import ApiV1RegionsCreateStateReasonErrorComponent
    from ..models.api_v1_regions_create_target_availability_error_component import (
        ApiV1RegionsCreateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_regions_create_tolerations_error_component import ApiV1RegionsCreateTolerationsErrorComponent


T = TypeVar("T", bound="ApiV1RegionsCreateValidationError")


@_attrs_define
class ApiV1RegionsCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1RegionsCreateActualAvailabilityErrorComponent | ApiV1RegionsCreateAnnotationsErrorComponent |
            ApiV1RegionsCreateArchivedAtErrorComponent | ApiV1RegionsCreateArchivedErrorComponent |
            ApiV1RegionsCreateArchivedReasonErrorComponent | ApiV1RegionsCreateConditionsErrorComponent |
            ApiV1RegionsCreateConfigErrorComponent | ApiV1RegionsCreateCriticalityErrorComponent |
            ApiV1RegionsCreateDebugModeErrorComponent | ApiV1RegionsCreateDiscoveryEnabledErrorComponent |
            ApiV1RegionsCreateDiscoveryRunningErrorComponent | ApiV1RegionsCreateDiscoveryTaskIdErrorComponent |
            ApiV1RegionsCreateDiscoveryTaskMetaErrorComponent | ApiV1RegionsCreateDisplayNameErrorComponent |
            ApiV1RegionsCreateKindErrorComponent | ApiV1RegionsCreateLabelsErrorComponent |
            ApiV1RegionsCreateLastStateChangeErrorComponent | ApiV1RegionsCreateLastStateErrorComponent |
            ApiV1RegionsCreateNameErrorComponent | ApiV1RegionsCreateNonFieldErrorsErrorComponent |
            ApiV1RegionsCreatePlatformFeaturesErrorComponent | ApiV1RegionsCreatePlatformFeaturesINDEXErrorComponent |
            ApiV1RegionsCreatePlatformServiceErrorComponent | ApiV1RegionsCreateProviderErrorComponent |
            ApiV1RegionsCreateProviderIdErrorComponent | ApiV1RegionsCreateProviderReferenceErrorComponent |
            ApiV1RegionsCreateReconciliationEnabledErrorComponent | ApiV1RegionsCreateReconciliationRunningErrorComponent |
            ApiV1RegionsCreateReconciliationTaskIdErrorComponent | ApiV1RegionsCreateReconciliationTaskMetaErrorComponent |
            ApiV1RegionsCreateRepairRunningErrorComponent | ApiV1RegionsCreateRepairTaskIdErrorComponent |
            ApiV1RegionsCreateRepairTaskMetaErrorComponent | ApiV1RegionsCreateScopeErrorComponent |
            ApiV1RegionsCreateSlaAvailabilityErrorComponent | ApiV1RegionsCreateSlaTargetErrorComponent |
            ApiV1RegionsCreateSloAvailabilityErrorComponent | ApiV1RegionsCreateSloTargetErrorComponent |
            ApiV1RegionsCreateStateErrorComponent | ApiV1RegionsCreateStateReasonErrorComponent |
            ApiV1RegionsCreateTargetAvailabilityErrorComponent | ApiV1RegionsCreateTolerationsErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1RegionsCreateActualAvailabilityErrorComponent
        | ApiV1RegionsCreateAnnotationsErrorComponent
        | ApiV1RegionsCreateArchivedAtErrorComponent
        | ApiV1RegionsCreateArchivedErrorComponent
        | ApiV1RegionsCreateArchivedReasonErrorComponent
        | ApiV1RegionsCreateConditionsErrorComponent
        | ApiV1RegionsCreateConfigErrorComponent
        | ApiV1RegionsCreateCriticalityErrorComponent
        | ApiV1RegionsCreateDebugModeErrorComponent
        | ApiV1RegionsCreateDiscoveryEnabledErrorComponent
        | ApiV1RegionsCreateDiscoveryRunningErrorComponent
        | ApiV1RegionsCreateDiscoveryTaskIdErrorComponent
        | ApiV1RegionsCreateDiscoveryTaskMetaErrorComponent
        | ApiV1RegionsCreateDisplayNameErrorComponent
        | ApiV1RegionsCreateKindErrorComponent
        | ApiV1RegionsCreateLabelsErrorComponent
        | ApiV1RegionsCreateLastStateChangeErrorComponent
        | ApiV1RegionsCreateLastStateErrorComponent
        | ApiV1RegionsCreateNameErrorComponent
        | ApiV1RegionsCreateNonFieldErrorsErrorComponent
        | ApiV1RegionsCreatePlatformFeaturesErrorComponent
        | ApiV1RegionsCreatePlatformFeaturesINDEXErrorComponent
        | ApiV1RegionsCreatePlatformServiceErrorComponent
        | ApiV1RegionsCreateProviderErrorComponent
        | ApiV1RegionsCreateProviderIdErrorComponent
        | ApiV1RegionsCreateProviderReferenceErrorComponent
        | ApiV1RegionsCreateReconciliationEnabledErrorComponent
        | ApiV1RegionsCreateReconciliationRunningErrorComponent
        | ApiV1RegionsCreateReconciliationTaskIdErrorComponent
        | ApiV1RegionsCreateReconciliationTaskMetaErrorComponent
        | ApiV1RegionsCreateRepairRunningErrorComponent
        | ApiV1RegionsCreateRepairTaskIdErrorComponent
        | ApiV1RegionsCreateRepairTaskMetaErrorComponent
        | ApiV1RegionsCreateScopeErrorComponent
        | ApiV1RegionsCreateSlaAvailabilityErrorComponent
        | ApiV1RegionsCreateSlaTargetErrorComponent
        | ApiV1RegionsCreateSloAvailabilityErrorComponent
        | ApiV1RegionsCreateSloTargetErrorComponent
        | ApiV1RegionsCreateStateErrorComponent
        | ApiV1RegionsCreateStateReasonErrorComponent
        | ApiV1RegionsCreateTargetAvailabilityErrorComponent
        | ApiV1RegionsCreateTolerationsErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_regions_create_actual_availability_error_component import (
            ApiV1RegionsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_create_annotations_error_component import (
            ApiV1RegionsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_regions_create_archived_at_error_component import (
            ApiV1RegionsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_regions_create_archived_error_component import ApiV1RegionsCreateArchivedErrorComponent
        from ..models.api_v1_regions_create_archived_reason_error_component import (
            ApiV1RegionsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_regions_create_conditions_error_component import ApiV1RegionsCreateConditionsErrorComponent
        from ..models.api_v1_regions_create_criticality_error_component import (
            ApiV1RegionsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_regions_create_debug_mode_error_component import ApiV1RegionsCreateDebugModeErrorComponent
        from ..models.api_v1_regions_create_discovery_enabled_error_component import (
            ApiV1RegionsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_regions_create_discovery_running_error_component import (
            ApiV1RegionsCreateDiscoveryRunningErrorComponent,
        )
        from ..models.api_v1_regions_create_discovery_task_id_error_component import (
            ApiV1RegionsCreateDiscoveryTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_create_discovery_task_meta_error_component import (
            ApiV1RegionsCreateDiscoveryTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_create_display_name_error_component import (
            ApiV1RegionsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_regions_create_kind_error_component import ApiV1RegionsCreateKindErrorComponent
        from ..models.api_v1_regions_create_labels_error_component import ApiV1RegionsCreateLabelsErrorComponent
        from ..models.api_v1_regions_create_last_state_change_error_component import (
            ApiV1RegionsCreateLastStateChangeErrorComponent,
        )
        from ..models.api_v1_regions_create_last_state_error_component import ApiV1RegionsCreateLastStateErrorComponent
        from ..models.api_v1_regions_create_name_error_component import ApiV1RegionsCreateNameErrorComponent
        from ..models.api_v1_regions_create_non_field_errors_error_component import (
            ApiV1RegionsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_regions_create_platform_features_error_component import (
            ApiV1RegionsCreatePlatformFeaturesErrorComponent,
        )
        from ..models.api_v1_regions_create_platform_features_index_error_component import (
            ApiV1RegionsCreatePlatformFeaturesINDEXErrorComponent,
        )
        from ..models.api_v1_regions_create_platform_service_error_component import (
            ApiV1RegionsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_regions_create_provider_error_component import ApiV1RegionsCreateProviderErrorComponent
        from ..models.api_v1_regions_create_provider_id_error_component import (
            ApiV1RegionsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_regions_create_provider_reference_error_component import (
            ApiV1RegionsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_regions_create_reconciliation_enabled_error_component import (
            ApiV1RegionsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_regions_create_reconciliation_running_error_component import (
            ApiV1RegionsCreateReconciliationRunningErrorComponent,
        )
        from ..models.api_v1_regions_create_reconciliation_task_id_error_component import (
            ApiV1RegionsCreateReconciliationTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_create_reconciliation_task_meta_error_component import (
            ApiV1RegionsCreateReconciliationTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_create_repair_running_error_component import (
            ApiV1RegionsCreateRepairRunningErrorComponent,
        )
        from ..models.api_v1_regions_create_repair_task_id_error_component import (
            ApiV1RegionsCreateRepairTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_create_repair_task_meta_error_component import (
            ApiV1RegionsCreateRepairTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_create_scope_error_component import ApiV1RegionsCreateScopeErrorComponent
        from ..models.api_v1_regions_create_sla_availability_error_component import (
            ApiV1RegionsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_create_sla_target_error_component import ApiV1RegionsCreateSlaTargetErrorComponent
        from ..models.api_v1_regions_create_slo_availability_error_component import (
            ApiV1RegionsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_create_slo_target_error_component import ApiV1RegionsCreateSloTargetErrorComponent
        from ..models.api_v1_regions_create_state_error_component import ApiV1RegionsCreateStateErrorComponent
        from ..models.api_v1_regions_create_state_reason_error_component import (
            ApiV1RegionsCreateStateReasonErrorComponent,
        )
        from ..models.api_v1_regions_create_target_availability_error_component import (
            ApiV1RegionsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_create_tolerations_error_component import (
            ApiV1RegionsCreateTolerationsErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1RegionsCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateStateReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateLastStateErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateLastStateChangeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateReconciliationRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateReconciliationTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateReconciliationTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateDiscoveryRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateDiscoveryTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateDiscoveryTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateRepairRunningErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateRepairTaskIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateRepairTaskMetaErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateConditionsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateTolerationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreatePlatformFeaturesErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1RegionsCreatePlatformFeaturesINDEXErrorComponent):
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
        from ..models.api_v1_regions_create_actual_availability_error_component import (
            ApiV1RegionsCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_create_annotations_error_component import (
            ApiV1RegionsCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_regions_create_archived_at_error_component import (
            ApiV1RegionsCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_regions_create_archived_error_component import ApiV1RegionsCreateArchivedErrorComponent
        from ..models.api_v1_regions_create_archived_reason_error_component import (
            ApiV1RegionsCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_regions_create_conditions_error_component import ApiV1RegionsCreateConditionsErrorComponent
        from ..models.api_v1_regions_create_config_error_component import ApiV1RegionsCreateConfigErrorComponent
        from ..models.api_v1_regions_create_criticality_error_component import (
            ApiV1RegionsCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_regions_create_debug_mode_error_component import ApiV1RegionsCreateDebugModeErrorComponent
        from ..models.api_v1_regions_create_discovery_enabled_error_component import (
            ApiV1RegionsCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_regions_create_discovery_running_error_component import (
            ApiV1RegionsCreateDiscoveryRunningErrorComponent,
        )
        from ..models.api_v1_regions_create_discovery_task_id_error_component import (
            ApiV1RegionsCreateDiscoveryTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_create_discovery_task_meta_error_component import (
            ApiV1RegionsCreateDiscoveryTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_create_display_name_error_component import (
            ApiV1RegionsCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_regions_create_kind_error_component import ApiV1RegionsCreateKindErrorComponent
        from ..models.api_v1_regions_create_labels_error_component import ApiV1RegionsCreateLabelsErrorComponent
        from ..models.api_v1_regions_create_last_state_change_error_component import (
            ApiV1RegionsCreateLastStateChangeErrorComponent,
        )
        from ..models.api_v1_regions_create_last_state_error_component import ApiV1RegionsCreateLastStateErrorComponent
        from ..models.api_v1_regions_create_name_error_component import ApiV1RegionsCreateNameErrorComponent
        from ..models.api_v1_regions_create_non_field_errors_error_component import (
            ApiV1RegionsCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_regions_create_platform_features_error_component import (
            ApiV1RegionsCreatePlatformFeaturesErrorComponent,
        )
        from ..models.api_v1_regions_create_platform_features_index_error_component import (
            ApiV1RegionsCreatePlatformFeaturesINDEXErrorComponent,
        )
        from ..models.api_v1_regions_create_platform_service_error_component import (
            ApiV1RegionsCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_regions_create_provider_error_component import ApiV1RegionsCreateProviderErrorComponent
        from ..models.api_v1_regions_create_provider_id_error_component import (
            ApiV1RegionsCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_regions_create_provider_reference_error_component import (
            ApiV1RegionsCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_regions_create_reconciliation_enabled_error_component import (
            ApiV1RegionsCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_regions_create_reconciliation_running_error_component import (
            ApiV1RegionsCreateReconciliationRunningErrorComponent,
        )
        from ..models.api_v1_regions_create_reconciliation_task_id_error_component import (
            ApiV1RegionsCreateReconciliationTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_create_reconciliation_task_meta_error_component import (
            ApiV1RegionsCreateReconciliationTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_create_repair_running_error_component import (
            ApiV1RegionsCreateRepairRunningErrorComponent,
        )
        from ..models.api_v1_regions_create_repair_task_id_error_component import (
            ApiV1RegionsCreateRepairTaskIdErrorComponent,
        )
        from ..models.api_v1_regions_create_repair_task_meta_error_component import (
            ApiV1RegionsCreateRepairTaskMetaErrorComponent,
        )
        from ..models.api_v1_regions_create_scope_error_component import ApiV1RegionsCreateScopeErrorComponent
        from ..models.api_v1_regions_create_sla_availability_error_component import (
            ApiV1RegionsCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_create_sla_target_error_component import ApiV1RegionsCreateSlaTargetErrorComponent
        from ..models.api_v1_regions_create_slo_availability_error_component import (
            ApiV1RegionsCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_create_slo_target_error_component import ApiV1RegionsCreateSloTargetErrorComponent
        from ..models.api_v1_regions_create_state_error_component import ApiV1RegionsCreateStateErrorComponent
        from ..models.api_v1_regions_create_state_reason_error_component import (
            ApiV1RegionsCreateStateReasonErrorComponent,
        )
        from ..models.api_v1_regions_create_target_availability_error_component import (
            ApiV1RegionsCreateTargetAvailabilityErrorComponent,
        )
        from ..models.api_v1_regions_create_tolerations_error_component import (
            ApiV1RegionsCreateTolerationsErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1RegionsCreateActualAvailabilityErrorComponent
                | ApiV1RegionsCreateAnnotationsErrorComponent
                | ApiV1RegionsCreateArchivedAtErrorComponent
                | ApiV1RegionsCreateArchivedErrorComponent
                | ApiV1RegionsCreateArchivedReasonErrorComponent
                | ApiV1RegionsCreateConditionsErrorComponent
                | ApiV1RegionsCreateConfigErrorComponent
                | ApiV1RegionsCreateCriticalityErrorComponent
                | ApiV1RegionsCreateDebugModeErrorComponent
                | ApiV1RegionsCreateDiscoveryEnabledErrorComponent
                | ApiV1RegionsCreateDiscoveryRunningErrorComponent
                | ApiV1RegionsCreateDiscoveryTaskIdErrorComponent
                | ApiV1RegionsCreateDiscoveryTaskMetaErrorComponent
                | ApiV1RegionsCreateDisplayNameErrorComponent
                | ApiV1RegionsCreateKindErrorComponent
                | ApiV1RegionsCreateLabelsErrorComponent
                | ApiV1RegionsCreateLastStateChangeErrorComponent
                | ApiV1RegionsCreateLastStateErrorComponent
                | ApiV1RegionsCreateNameErrorComponent
                | ApiV1RegionsCreateNonFieldErrorsErrorComponent
                | ApiV1RegionsCreatePlatformFeaturesErrorComponent
                | ApiV1RegionsCreatePlatformFeaturesINDEXErrorComponent
                | ApiV1RegionsCreatePlatformServiceErrorComponent
                | ApiV1RegionsCreateProviderErrorComponent
                | ApiV1RegionsCreateProviderIdErrorComponent
                | ApiV1RegionsCreateProviderReferenceErrorComponent
                | ApiV1RegionsCreateReconciliationEnabledErrorComponent
                | ApiV1RegionsCreateReconciliationRunningErrorComponent
                | ApiV1RegionsCreateReconciliationTaskIdErrorComponent
                | ApiV1RegionsCreateReconciliationTaskMetaErrorComponent
                | ApiV1RegionsCreateRepairRunningErrorComponent
                | ApiV1RegionsCreateRepairTaskIdErrorComponent
                | ApiV1RegionsCreateRepairTaskMetaErrorComponent
                | ApiV1RegionsCreateScopeErrorComponent
                | ApiV1RegionsCreateSlaAvailabilityErrorComponent
                | ApiV1RegionsCreateSlaTargetErrorComponent
                | ApiV1RegionsCreateSloAvailabilityErrorComponent
                | ApiV1RegionsCreateSloTargetErrorComponent
                | ApiV1RegionsCreateStateErrorComponent
                | ApiV1RegionsCreateStateReasonErrorComponent
                | ApiV1RegionsCreateTargetAvailabilityErrorComponent
                | ApiV1RegionsCreateTolerationsErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_0 = (
                        ApiV1RegionsCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_1 = (
                        ApiV1RegionsCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_2 = (
                        ApiV1RegionsCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_3 = (
                        ApiV1RegionsCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_4 = (
                        ApiV1RegionsCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_5 = (
                        ApiV1RegionsCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_6 = (
                        ApiV1RegionsCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_7 = (
                        ApiV1RegionsCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_8 = (
                        ApiV1RegionsCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_9 = (
                        ApiV1RegionsCreateStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_10 = (
                        ApiV1RegionsCreateStateReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_11 = (
                        ApiV1RegionsCreateLastStateErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_12 = (
                        ApiV1RegionsCreateLastStateChangeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_13 = (
                        ApiV1RegionsCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_14 = (
                        ApiV1RegionsCreateReconciliationRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_15 = (
                        ApiV1RegionsCreateReconciliationTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_16 = (
                        ApiV1RegionsCreateReconciliationTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_17 = (
                        ApiV1RegionsCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_18 = (
                        ApiV1RegionsCreateDiscoveryRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_19 = (
                        ApiV1RegionsCreateDiscoveryTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_20 = (
                        ApiV1RegionsCreateDiscoveryTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_21 = (
                        ApiV1RegionsCreateRepairRunningErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_22 = (
                        ApiV1RegionsCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_23 = (
                        ApiV1RegionsCreateRepairTaskIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_24 = (
                        ApiV1RegionsCreateRepairTaskMetaErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_25 = (
                        ApiV1RegionsCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_26 = (
                        ApiV1RegionsCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_27 = (
                        ApiV1RegionsCreateConditionsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_28 = (
                        ApiV1RegionsCreateTolerationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_29 = (
                        ApiV1RegionsCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_30 = (
                        ApiV1RegionsCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_31 = (
                        ApiV1RegionsCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_32 = (
                        ApiV1RegionsCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_33 = (
                        ApiV1RegionsCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_34 = (
                        ApiV1RegionsCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_35 = (
                        ApiV1RegionsCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_36 = (
                        ApiV1RegionsCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_37 = (
                        ApiV1RegionsCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_38 = (
                        ApiV1RegionsCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_38
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_39 = (
                        ApiV1RegionsCreatePlatformFeaturesErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_39
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_regions_create_error_type_40 = (
                        ApiV1RegionsCreatePlatformFeaturesINDEXErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_regions_create_error_type_40
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_regions_create_error_type_41 = (
                    ApiV1RegionsCreateConfigErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_regions_create_error_type_41

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_regions_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_regions_create_validation_error.additional_properties = d
        return api_v1_regions_create_validation_error

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
