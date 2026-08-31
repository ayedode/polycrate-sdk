from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_controlplanes_create_actual_availability_error_component import (
        ApiV1KubernetesControlplanesCreateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_annotations_error_component import (
        ApiV1KubernetesControlplanesCreateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_archived_at_error_component import (
        ApiV1KubernetesControlplanesCreateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_archived_error_component import (
        ApiV1KubernetesControlplanesCreateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_archived_reason_error_component import (
        ApiV1KubernetesControlplanesCreateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_cluster_domain_error_component import (
        ApiV1KubernetesControlplanesCreateClusterDomainErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_criticality_error_component import (
        ApiV1KubernetesControlplanesCreateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_debug_mode_error_component import (
        ApiV1KubernetesControlplanesCreateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_discovery_enabled_error_component import (
        ApiV1KubernetesControlplanesCreateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_display_name_error_component import (
        ApiV1KubernetesControlplanesCreateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_kind_error_component import (
        ApiV1KubernetesControlplanesCreateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_labels_error_component import (
        ApiV1KubernetesControlplanesCreateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_loadbalancer_mode_error_component import (
        ApiV1KubernetesControlplanesCreateLoadbalancerModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_loadbalancer_provider_error_component import (
        ApiV1KubernetesControlplanesCreateLoadbalancerProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_name_error_component import (
        ApiV1KubernetesControlplanesCreateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_non_field_errors_error_component import (
        ApiV1KubernetesControlplanesCreateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_persistence_size_error_component import (
        ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_platform_service_error_component import (
        ApiV1KubernetesControlplanesCreatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_provider_error_component import (
        ApiV1KubernetesControlplanesCreateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_provider_id_error_component import (
        ApiV1KubernetesControlplanesCreateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_provider_reference_error_component import (
        ApiV1KubernetesControlplanesCreateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_reconciliation_enabled_error_component import (
        ApiV1KubernetesControlplanesCreateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_scope_error_component import (
        ApiV1KubernetesControlplanesCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_sla_availability_error_component import (
        ApiV1KubernetesControlplanesCreateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_sla_target_error_component import (
        ApiV1KubernetesControlplanesCreateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_slo_availability_error_component import (
        ApiV1KubernetesControlplanesCreateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_slo_target_error_component import (
        ApiV1KubernetesControlplanesCreateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_storage_class_error_component import (
        ApiV1KubernetesControlplanesCreateStorageClassErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_target_availability_error_component import (
        ApiV1KubernetesControlplanesCreateTargetAvailabilityErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesControlplanesCreateValidationError")


@_attrs_define
class ApiV1KubernetesControlplanesCreateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesControlplanesCreateActualAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesCreateAnnotationsErrorComponent |
            ApiV1KubernetesControlplanesCreateArchivedAtErrorComponent |
            ApiV1KubernetesControlplanesCreateArchivedErrorComponent |
            ApiV1KubernetesControlplanesCreateArchivedReasonErrorComponent |
            ApiV1KubernetesControlplanesCreateClusterDomainErrorComponent |
            ApiV1KubernetesControlplanesCreateCriticalityErrorComponent |
            ApiV1KubernetesControlplanesCreateDebugModeErrorComponent |
            ApiV1KubernetesControlplanesCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesControlplanesCreateDisplayNameErrorComponent |
            ApiV1KubernetesControlplanesCreateKindErrorComponent | ApiV1KubernetesControlplanesCreateLabelsErrorComponent |
            ApiV1KubernetesControlplanesCreateLoadbalancerModeErrorComponent |
            ApiV1KubernetesControlplanesCreateLoadbalancerProviderErrorComponent |
            ApiV1KubernetesControlplanesCreateNameErrorComponent |
            ApiV1KubernetesControlplanesCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponent |
            ApiV1KubernetesControlplanesCreatePlatformServiceErrorComponent |
            ApiV1KubernetesControlplanesCreateProviderErrorComponent |
            ApiV1KubernetesControlplanesCreateProviderIdErrorComponent |
            ApiV1KubernetesControlplanesCreateProviderReferenceErrorComponent |
            ApiV1KubernetesControlplanesCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesControlplanesCreateScopeErrorComponent |
            ApiV1KubernetesControlplanesCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesCreateSlaTargetErrorComponent |
            ApiV1KubernetesControlplanesCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesCreateSloTargetErrorComponent |
            ApiV1KubernetesControlplanesCreateStorageClassErrorComponent |
            ApiV1KubernetesControlplanesCreateTargetAvailabilityErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesControlplanesCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesCreateAnnotationsErrorComponent
        | ApiV1KubernetesControlplanesCreateArchivedAtErrorComponent
        | ApiV1KubernetesControlplanesCreateArchivedErrorComponent
        | ApiV1KubernetesControlplanesCreateArchivedReasonErrorComponent
        | ApiV1KubernetesControlplanesCreateClusterDomainErrorComponent
        | ApiV1KubernetesControlplanesCreateCriticalityErrorComponent
        | ApiV1KubernetesControlplanesCreateDebugModeErrorComponent
        | ApiV1KubernetesControlplanesCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesControlplanesCreateDisplayNameErrorComponent
        | ApiV1KubernetesControlplanesCreateKindErrorComponent
        | ApiV1KubernetesControlplanesCreateLabelsErrorComponent
        | ApiV1KubernetesControlplanesCreateLoadbalancerModeErrorComponent
        | ApiV1KubernetesControlplanesCreateLoadbalancerProviderErrorComponent
        | ApiV1KubernetesControlplanesCreateNameErrorComponent
        | ApiV1KubernetesControlplanesCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponent
        | ApiV1KubernetesControlplanesCreatePlatformServiceErrorComponent
        | ApiV1KubernetesControlplanesCreateProviderErrorComponent
        | ApiV1KubernetesControlplanesCreateProviderIdErrorComponent
        | ApiV1KubernetesControlplanesCreateProviderReferenceErrorComponent
        | ApiV1KubernetesControlplanesCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesControlplanesCreateScopeErrorComponent
        | ApiV1KubernetesControlplanesCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesCreateSlaTargetErrorComponent
        | ApiV1KubernetesControlplanesCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesCreateSloTargetErrorComponent
        | ApiV1KubernetesControlplanesCreateStorageClassErrorComponent
        | ApiV1KubernetesControlplanesCreateTargetAvailabilityErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_controlplanes_create_actual_availability_error_component import (
            ApiV1KubernetesControlplanesCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_annotations_error_component import (
            ApiV1KubernetesControlplanesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_archived_at_error_component import (
            ApiV1KubernetesControlplanesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_archived_error_component import (
            ApiV1KubernetesControlplanesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_archived_reason_error_component import (
            ApiV1KubernetesControlplanesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_criticality_error_component import (
            ApiV1KubernetesControlplanesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_debug_mode_error_component import (
            ApiV1KubernetesControlplanesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_discovery_enabled_error_component import (
            ApiV1KubernetesControlplanesCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_display_name_error_component import (
            ApiV1KubernetesControlplanesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_kind_error_component import (
            ApiV1KubernetesControlplanesCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_labels_error_component import (
            ApiV1KubernetesControlplanesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_loadbalancer_mode_error_component import (
            ApiV1KubernetesControlplanesCreateLoadbalancerModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_loadbalancer_provider_error_component import (
            ApiV1KubernetesControlplanesCreateLoadbalancerProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_name_error_component import (
            ApiV1KubernetesControlplanesCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_non_field_errors_error_component import (
            ApiV1KubernetesControlplanesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_persistence_size_error_component import (
            ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_platform_service_error_component import (
            ApiV1KubernetesControlplanesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_provider_error_component import (
            ApiV1KubernetesControlplanesCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_provider_id_error_component import (
            ApiV1KubernetesControlplanesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_provider_reference_error_component import (
            ApiV1KubernetesControlplanesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesControlplanesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_scope_error_component import (
            ApiV1KubernetesControlplanesCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_sla_availability_error_component import (
            ApiV1KubernetesControlplanesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_sla_target_error_component import (
            ApiV1KubernetesControlplanesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_slo_availability_error_component import (
            ApiV1KubernetesControlplanesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_slo_target_error_component import (
            ApiV1KubernetesControlplanesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_storage_class_error_component import (
            ApiV1KubernetesControlplanesCreateStorageClassErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_target_availability_error_component import (
            ApiV1KubernetesControlplanesCreateTargetAvailabilityErrorComponent,
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateLoadbalancerModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateLoadbalancerProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateStorageClassErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponent):
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
        from ..models.api_v1_kubernetes_controlplanes_create_actual_availability_error_component import (
            ApiV1KubernetesControlplanesCreateActualAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_annotations_error_component import (
            ApiV1KubernetesControlplanesCreateAnnotationsErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_archived_at_error_component import (
            ApiV1KubernetesControlplanesCreateArchivedAtErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_archived_error_component import (
            ApiV1KubernetesControlplanesCreateArchivedErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_archived_reason_error_component import (
            ApiV1KubernetesControlplanesCreateArchivedReasonErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_cluster_domain_error_component import (
            ApiV1KubernetesControlplanesCreateClusterDomainErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_criticality_error_component import (
            ApiV1KubernetesControlplanesCreateCriticalityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_debug_mode_error_component import (
            ApiV1KubernetesControlplanesCreateDebugModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_discovery_enabled_error_component import (
            ApiV1KubernetesControlplanesCreateDiscoveryEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_display_name_error_component import (
            ApiV1KubernetesControlplanesCreateDisplayNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_kind_error_component import (
            ApiV1KubernetesControlplanesCreateKindErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_labels_error_component import (
            ApiV1KubernetesControlplanesCreateLabelsErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_loadbalancer_mode_error_component import (
            ApiV1KubernetesControlplanesCreateLoadbalancerModeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_loadbalancer_provider_error_component import (
            ApiV1KubernetesControlplanesCreateLoadbalancerProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_name_error_component import (
            ApiV1KubernetesControlplanesCreateNameErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_non_field_errors_error_component import (
            ApiV1KubernetesControlplanesCreateNonFieldErrorsErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_persistence_size_error_component import (
            ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_platform_service_error_component import (
            ApiV1KubernetesControlplanesCreatePlatformServiceErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_provider_error_component import (
            ApiV1KubernetesControlplanesCreateProviderErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_provider_id_error_component import (
            ApiV1KubernetesControlplanesCreateProviderIdErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_provider_reference_error_component import (
            ApiV1KubernetesControlplanesCreateProviderReferenceErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesControlplanesCreateReconciliationEnabledErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_scope_error_component import (
            ApiV1KubernetesControlplanesCreateScopeErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_sla_availability_error_component import (
            ApiV1KubernetesControlplanesCreateSlaAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_sla_target_error_component import (
            ApiV1KubernetesControlplanesCreateSlaTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_slo_availability_error_component import (
            ApiV1KubernetesControlplanesCreateSloAvailabilityErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_slo_target_error_component import (
            ApiV1KubernetesControlplanesCreateSloTargetErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_storage_class_error_component import (
            ApiV1KubernetesControlplanesCreateStorageClassErrorComponent,
        )
        from ..models.api_v1_kubernetes_controlplanes_create_target_availability_error_component import (
            ApiV1KubernetesControlplanesCreateTargetAvailabilityErrorComponent,
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesControlplanesCreateActualAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesCreateAnnotationsErrorComponent
                | ApiV1KubernetesControlplanesCreateArchivedAtErrorComponent
                | ApiV1KubernetesControlplanesCreateArchivedErrorComponent
                | ApiV1KubernetesControlplanesCreateArchivedReasonErrorComponent
                | ApiV1KubernetesControlplanesCreateClusterDomainErrorComponent
                | ApiV1KubernetesControlplanesCreateCriticalityErrorComponent
                | ApiV1KubernetesControlplanesCreateDebugModeErrorComponent
                | ApiV1KubernetesControlplanesCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesControlplanesCreateDisplayNameErrorComponent
                | ApiV1KubernetesControlplanesCreateKindErrorComponent
                | ApiV1KubernetesControlplanesCreateLabelsErrorComponent
                | ApiV1KubernetesControlplanesCreateLoadbalancerModeErrorComponent
                | ApiV1KubernetesControlplanesCreateLoadbalancerProviderErrorComponent
                | ApiV1KubernetesControlplanesCreateNameErrorComponent
                | ApiV1KubernetesControlplanesCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponent
                | ApiV1KubernetesControlplanesCreatePlatformServiceErrorComponent
                | ApiV1KubernetesControlplanesCreateProviderErrorComponent
                | ApiV1KubernetesControlplanesCreateProviderIdErrorComponent
                | ApiV1KubernetesControlplanesCreateProviderReferenceErrorComponent
                | ApiV1KubernetesControlplanesCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesControlplanesCreateScopeErrorComponent
                | ApiV1KubernetesControlplanesCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesCreateSlaTargetErrorComponent
                | ApiV1KubernetesControlplanesCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesCreateSloTargetErrorComponent
                | ApiV1KubernetesControlplanesCreateStorageClassErrorComponent
                | ApiV1KubernetesControlplanesCreateTargetAvailabilityErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_0 = (
                        ApiV1KubernetesControlplanesCreateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_1 = (
                        ApiV1KubernetesControlplanesCreateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_2 = (
                        ApiV1KubernetesControlplanesCreateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_3 = (
                        ApiV1KubernetesControlplanesCreateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_4 = (
                        ApiV1KubernetesControlplanesCreateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_5 = (
                        ApiV1KubernetesControlplanesCreateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_6 = (
                        ApiV1KubernetesControlplanesCreateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_7 = (
                        ApiV1KubernetesControlplanesCreateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_8 = (
                        ApiV1KubernetesControlplanesCreateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_9 = (
                        ApiV1KubernetesControlplanesCreateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_10 = (
                        ApiV1KubernetesControlplanesCreateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_11 = (
                        ApiV1KubernetesControlplanesCreatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_12 = (
                        ApiV1KubernetesControlplanesCreateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_13 = (
                        ApiV1KubernetesControlplanesCreateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_14 = (
                        ApiV1KubernetesControlplanesCreateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_15 = (
                        ApiV1KubernetesControlplanesCreateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_16 = (
                        ApiV1KubernetesControlplanesCreateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_17 = (
                        ApiV1KubernetesControlplanesCreateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_18 = (
                        ApiV1KubernetesControlplanesCreateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_19 = (
                        ApiV1KubernetesControlplanesCreateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_20 = (
                        ApiV1KubernetesControlplanesCreateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_21 = (
                        ApiV1KubernetesControlplanesCreateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_22 = (
                        ApiV1KubernetesControlplanesCreateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_23 = (
                        ApiV1KubernetesControlplanesCreateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_24 = (
                        ApiV1KubernetesControlplanesCreateLoadbalancerModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_25 = (
                        ApiV1KubernetesControlplanesCreateLoadbalancerProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_26 = (
                        ApiV1KubernetesControlplanesCreateStorageClassErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_27 = (
                        ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_28 = (
                    ApiV1KubernetesControlplanesCreateClusterDomainErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_28

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_controlplanes_create_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_controlplanes_create_validation_error.additional_properties = d
        return api_v1_kubernetes_controlplanes_create_validation_error

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
