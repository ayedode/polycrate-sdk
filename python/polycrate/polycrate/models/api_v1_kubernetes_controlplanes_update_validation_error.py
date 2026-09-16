from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_controlplanes_update_actual_availability_error_component import (
        ApiV1KubernetesControlplanesUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_annotations_error_component import (
        ApiV1KubernetesControlplanesUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_archived_at_error_component import (
        ApiV1KubernetesControlplanesUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_archived_error_component import (
        ApiV1KubernetesControlplanesUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_archived_reason_error_component import (
        ApiV1KubernetesControlplanesUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_audit_logging_enabled_error_component import (
        ApiV1KubernetesControlplanesUpdateAuditLoggingEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_cluster_domain_error_component import (
        ApiV1KubernetesControlplanesUpdateClusterDomainErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_criticality_error_component import (
        ApiV1KubernetesControlplanesUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_debug_mode_error_component import (
        ApiV1KubernetesControlplanesUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_discovery_enabled_error_component import (
        ApiV1KubernetesControlplanesUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_display_name_error_component import (
        ApiV1KubernetesControlplanesUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_exposure_type_error_component import (
        ApiV1KubernetesControlplanesUpdateExposureTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_gateway_class_name_error_component import (
        ApiV1KubernetesControlplanesUpdateGatewayClassNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_kind_error_component import (
        ApiV1KubernetesControlplanesUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_labels_error_component import (
        ApiV1KubernetesControlplanesUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_loadbalancer_mode_error_component import (
        ApiV1KubernetesControlplanesUpdateLoadbalancerModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_loadbalancer_provider_error_component import (
        ApiV1KubernetesControlplanesUpdateLoadbalancerProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_name_error_component import (
        ApiV1KubernetesControlplanesUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_non_field_errors_error_component import (
        ApiV1KubernetesControlplanesUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_organization_id_error_component import (
        ApiV1KubernetesControlplanesUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_parent_gateway_name_error_component import (
        ApiV1KubernetesControlplanesUpdateParentGatewayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_parent_gateway_namespace_error_component import (
        ApiV1KubernetesControlplanesUpdateParentGatewayNamespaceErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_parent_gateway_section_name_error_component import (
        ApiV1KubernetesControlplanesUpdateParentGatewaySectionNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_persistence_size_error_component import (
        ApiV1KubernetesControlplanesUpdatePersistenceSizeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_platform_service_error_component import (
        ApiV1KubernetesControlplanesUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_provider_error_component import (
        ApiV1KubernetesControlplanesUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_provider_id_error_component import (
        ApiV1KubernetesControlplanesUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_provider_reference_error_component import (
        ApiV1KubernetesControlplanesUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesControlplanesUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_region_id_error_component import (
        ApiV1KubernetesControlplanesUpdateRegionIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_scope_error_component import (
        ApiV1KubernetesControlplanesUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_secrets_encryption_enabled_error_component import (
        ApiV1KubernetesControlplanesUpdateSecretsEncryptionEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_sla_availability_error_component import (
        ApiV1KubernetesControlplanesUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_sla_target_error_component import (
        ApiV1KubernetesControlplanesUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_slo_availability_error_component import (
        ApiV1KubernetesControlplanesUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_slo_target_error_component import (
        ApiV1KubernetesControlplanesUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_storage_class_error_component import (
        ApiV1KubernetesControlplanesUpdateStorageClassErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_target_availability_error_component import (
        ApiV1KubernetesControlplanesUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_update_workspace_id_error_component import (
        ApiV1KubernetesControlplanesUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesControlplanesUpdateValidationError")


@_attrs_define
class ApiV1KubernetesControlplanesUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesControlplanesUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesUpdateAnnotationsErrorComponent |
            ApiV1KubernetesControlplanesUpdateArchivedAtErrorComponent |
            ApiV1KubernetesControlplanesUpdateArchivedErrorComponent |
            ApiV1KubernetesControlplanesUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesControlplanesUpdateAuditLoggingEnabledErrorComponent |
            ApiV1KubernetesControlplanesUpdateClusterDomainErrorComponent |
            ApiV1KubernetesControlplanesUpdateCriticalityErrorComponent |
            ApiV1KubernetesControlplanesUpdateDebugModeErrorComponent |
            ApiV1KubernetesControlplanesUpdateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesControlplanesUpdateDisplayNameErrorComponent |
            ApiV1KubernetesControlplanesUpdateExposureTypeErrorComponent |
            ApiV1KubernetesControlplanesUpdateGatewayClassNameErrorComponent |
            ApiV1KubernetesControlplanesUpdateKindErrorComponent | ApiV1KubernetesControlplanesUpdateLabelsErrorComponent |
            ApiV1KubernetesControlplanesUpdateLoadbalancerModeErrorComponent |
            ApiV1KubernetesControlplanesUpdateLoadbalancerProviderErrorComponent |
            ApiV1KubernetesControlplanesUpdateNameErrorComponent |
            ApiV1KubernetesControlplanesUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesControlplanesUpdateOrganizationIdErrorComponent |
            ApiV1KubernetesControlplanesUpdateParentGatewayNameErrorComponent |
            ApiV1KubernetesControlplanesUpdateParentGatewayNamespaceErrorComponent |
            ApiV1KubernetesControlplanesUpdateParentGatewaySectionNameErrorComponent |
            ApiV1KubernetesControlplanesUpdatePersistenceSizeErrorComponent |
            ApiV1KubernetesControlplanesUpdatePlatformServiceErrorComponent |
            ApiV1KubernetesControlplanesUpdateProviderErrorComponent |
            ApiV1KubernetesControlplanesUpdateProviderIdErrorComponent |
            ApiV1KubernetesControlplanesUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesControlplanesUpdateReconciliationEnabledErrorComponent |
            ApiV1KubernetesControlplanesUpdateRegionIdErrorComponent | ApiV1KubernetesControlplanesUpdateScopeErrorComponent
            | ApiV1KubernetesControlplanesUpdateSecretsEncryptionEnabledErrorComponent |
            ApiV1KubernetesControlplanesUpdateSlaAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesUpdateSlaTargetErrorComponent |
            ApiV1KubernetesControlplanesUpdateSloAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesUpdateSloTargetErrorComponent |
            ApiV1KubernetesControlplanesUpdateStorageClassErrorComponent |
            ApiV1KubernetesControlplanesUpdateTargetAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesControlplanesUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesUpdateAnnotationsErrorComponent
        | ApiV1KubernetesControlplanesUpdateArchivedAtErrorComponent
        | ApiV1KubernetesControlplanesUpdateArchivedErrorComponent
        | ApiV1KubernetesControlplanesUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesControlplanesUpdateAuditLoggingEnabledErrorComponent
        | ApiV1KubernetesControlplanesUpdateClusterDomainErrorComponent
        | ApiV1KubernetesControlplanesUpdateCriticalityErrorComponent
        | ApiV1KubernetesControlplanesUpdateDebugModeErrorComponent
        | ApiV1KubernetesControlplanesUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesControlplanesUpdateDisplayNameErrorComponent
        | ApiV1KubernetesControlplanesUpdateExposureTypeErrorComponent
        | ApiV1KubernetesControlplanesUpdateGatewayClassNameErrorComponent
        | ApiV1KubernetesControlplanesUpdateKindErrorComponent
        | ApiV1KubernetesControlplanesUpdateLabelsErrorComponent
        | ApiV1KubernetesControlplanesUpdateLoadbalancerModeErrorComponent
        | ApiV1KubernetesControlplanesUpdateLoadbalancerProviderErrorComponent
        | ApiV1KubernetesControlplanesUpdateNameErrorComponent
        | ApiV1KubernetesControlplanesUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesControlplanesUpdateOrganizationIdErrorComponent
        | ApiV1KubernetesControlplanesUpdateParentGatewayNameErrorComponent
        | ApiV1KubernetesControlplanesUpdateParentGatewayNamespaceErrorComponent
        | ApiV1KubernetesControlplanesUpdateParentGatewaySectionNameErrorComponent
        | ApiV1KubernetesControlplanesUpdatePersistenceSizeErrorComponent
        | ApiV1KubernetesControlplanesUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesControlplanesUpdateProviderErrorComponent
        | ApiV1KubernetesControlplanesUpdateProviderIdErrorComponent
        | ApiV1KubernetesControlplanesUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesControlplanesUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesControlplanesUpdateRegionIdErrorComponent
        | ApiV1KubernetesControlplanesUpdateScopeErrorComponent
        | ApiV1KubernetesControlplanesUpdateSecretsEncryptionEnabledErrorComponent
        | ApiV1KubernetesControlplanesUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesUpdateSlaTargetErrorComponent
        | ApiV1KubernetesControlplanesUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesUpdateSloTargetErrorComponent
        | ApiV1KubernetesControlplanesUpdateStorageClassErrorComponent
        | ApiV1KubernetesControlplanesUpdateTargetAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_controlplanes_update_actual_availability_error_component import (
            ApiV1KubernetesControlplanesUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_annotations_error_component import (
            ApiV1KubernetesControlplanesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_archived_at_error_component import (
            ApiV1KubernetesControlplanesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_archived_error_component import (
            ApiV1KubernetesControlplanesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_archived_reason_error_component import (
            ApiV1KubernetesControlplanesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_audit_logging_enabled_error_component import (
            ApiV1KubernetesControlplanesUpdateAuditLoggingEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_criticality_error_component import (
            ApiV1KubernetesControlplanesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_debug_mode_error_component import (
            ApiV1KubernetesControlplanesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_discovery_enabled_error_component import (
            ApiV1KubernetesControlplanesUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_display_name_error_component import (
            ApiV1KubernetesControlplanesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_exposure_type_error_component import (
            ApiV1KubernetesControlplanesUpdateExposureTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_gateway_class_name_error_component import (
            ApiV1KubernetesControlplanesUpdateGatewayClassNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_kind_error_component import (
            ApiV1KubernetesControlplanesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_labels_error_component import (
            ApiV1KubernetesControlplanesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_loadbalancer_mode_error_component import (
            ApiV1KubernetesControlplanesUpdateLoadbalancerModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_loadbalancer_provider_error_component import (
            ApiV1KubernetesControlplanesUpdateLoadbalancerProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_name_error_component import (
            ApiV1KubernetesControlplanesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_non_field_errors_error_component import (
            ApiV1KubernetesControlplanesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_organization_id_error_component import (
            ApiV1KubernetesControlplanesUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_parent_gateway_name_error_component import (
            ApiV1KubernetesControlplanesUpdateParentGatewayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_parent_gateway_namespace_error_component import (
            ApiV1KubernetesControlplanesUpdateParentGatewayNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_parent_gateway_section_name_error_component import (
            ApiV1KubernetesControlplanesUpdateParentGatewaySectionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_persistence_size_error_component import (
            ApiV1KubernetesControlplanesUpdatePersistenceSizeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_platform_service_error_component import (
            ApiV1KubernetesControlplanesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_provider_error_component import (
            ApiV1KubernetesControlplanesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_provider_id_error_component import (
            ApiV1KubernetesControlplanesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_provider_reference_error_component import (
            ApiV1KubernetesControlplanesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesControlplanesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_region_id_error_component import (
            ApiV1KubernetesControlplanesUpdateRegionIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_scope_error_component import (
            ApiV1KubernetesControlplanesUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_secrets_encryption_enabled_error_component import (
            ApiV1KubernetesControlplanesUpdateSecretsEncryptionEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_sla_availability_error_component import (
            ApiV1KubernetesControlplanesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_sla_target_error_component import (
            ApiV1KubernetesControlplanesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_slo_availability_error_component import (
            ApiV1KubernetesControlplanesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_slo_target_error_component import (
            ApiV1KubernetesControlplanesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_storage_class_error_component import (
            ApiV1KubernetesControlplanesUpdateStorageClassErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_target_availability_error_component import (
            ApiV1KubernetesControlplanesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_workspace_id_error_component import (
            ApiV1KubernetesControlplanesUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateReconciliationEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateTargetAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateActualAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateRegionIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateLoadbalancerModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateLoadbalancerProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateExposureTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateParentGatewayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateParentGatewayNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateParentGatewaySectionNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateGatewayClassNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateAuditLoggingEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateSecretsEncryptionEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdateStorageClassErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesUpdatePersistenceSizeErrorComponent):
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
        from ..models.api_v1_kubernetes_controlplanes_update_actual_availability_error_component import (
            ApiV1KubernetesControlplanesUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_annotations_error_component import (
            ApiV1KubernetesControlplanesUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_archived_at_error_component import (
            ApiV1KubernetesControlplanesUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_archived_error_component import (
            ApiV1KubernetesControlplanesUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_archived_reason_error_component import (
            ApiV1KubernetesControlplanesUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_audit_logging_enabled_error_component import (
            ApiV1KubernetesControlplanesUpdateAuditLoggingEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_cluster_domain_error_component import (
            ApiV1KubernetesControlplanesUpdateClusterDomainErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_criticality_error_component import (
            ApiV1KubernetesControlplanesUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_debug_mode_error_component import (
            ApiV1KubernetesControlplanesUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_discovery_enabled_error_component import (
            ApiV1KubernetesControlplanesUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_display_name_error_component import (
            ApiV1KubernetesControlplanesUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_exposure_type_error_component import (
            ApiV1KubernetesControlplanesUpdateExposureTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_gateway_class_name_error_component import (
            ApiV1KubernetesControlplanesUpdateGatewayClassNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_kind_error_component import (
            ApiV1KubernetesControlplanesUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_labels_error_component import (
            ApiV1KubernetesControlplanesUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_loadbalancer_mode_error_component import (
            ApiV1KubernetesControlplanesUpdateLoadbalancerModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_loadbalancer_provider_error_component import (
            ApiV1KubernetesControlplanesUpdateLoadbalancerProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_name_error_component import (
            ApiV1KubernetesControlplanesUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_non_field_errors_error_component import (
            ApiV1KubernetesControlplanesUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_organization_id_error_component import (
            ApiV1KubernetesControlplanesUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_parent_gateway_name_error_component import (
            ApiV1KubernetesControlplanesUpdateParentGatewayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_parent_gateway_namespace_error_component import (
            ApiV1KubernetesControlplanesUpdateParentGatewayNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_parent_gateway_section_name_error_component import (
            ApiV1KubernetesControlplanesUpdateParentGatewaySectionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_persistence_size_error_component import (
            ApiV1KubernetesControlplanesUpdatePersistenceSizeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_platform_service_error_component import (
            ApiV1KubernetesControlplanesUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_provider_error_component import (
            ApiV1KubernetesControlplanesUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_provider_id_error_component import (
            ApiV1KubernetesControlplanesUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_provider_reference_error_component import (
            ApiV1KubernetesControlplanesUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesControlplanesUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_region_id_error_component import (
            ApiV1KubernetesControlplanesUpdateRegionIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_scope_error_component import (
            ApiV1KubernetesControlplanesUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_secrets_encryption_enabled_error_component import (
            ApiV1KubernetesControlplanesUpdateSecretsEncryptionEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_sla_availability_error_component import (
            ApiV1KubernetesControlplanesUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_sla_target_error_component import (
            ApiV1KubernetesControlplanesUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_slo_availability_error_component import (
            ApiV1KubernetesControlplanesUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_slo_target_error_component import (
            ApiV1KubernetesControlplanesUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_storage_class_error_component import (
            ApiV1KubernetesControlplanesUpdateStorageClassErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_target_availability_error_component import (
            ApiV1KubernetesControlplanesUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_update_workspace_id_error_component import (
            ApiV1KubernetesControlplanesUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesControlplanesUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesUpdateAnnotationsErrorComponent
                | ApiV1KubernetesControlplanesUpdateArchivedAtErrorComponent
                | ApiV1KubernetesControlplanesUpdateArchivedErrorComponent
                | ApiV1KubernetesControlplanesUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesControlplanesUpdateAuditLoggingEnabledErrorComponent
                | ApiV1KubernetesControlplanesUpdateClusterDomainErrorComponent
                | ApiV1KubernetesControlplanesUpdateCriticalityErrorComponent
                | ApiV1KubernetesControlplanesUpdateDebugModeErrorComponent
                | ApiV1KubernetesControlplanesUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesControlplanesUpdateDisplayNameErrorComponent
                | ApiV1KubernetesControlplanesUpdateExposureTypeErrorComponent
                | ApiV1KubernetesControlplanesUpdateGatewayClassNameErrorComponent
                | ApiV1KubernetesControlplanesUpdateKindErrorComponent
                | ApiV1KubernetesControlplanesUpdateLabelsErrorComponent
                | ApiV1KubernetesControlplanesUpdateLoadbalancerModeErrorComponent
                | ApiV1KubernetesControlplanesUpdateLoadbalancerProviderErrorComponent
                | ApiV1KubernetesControlplanesUpdateNameErrorComponent
                | ApiV1KubernetesControlplanesUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesControlplanesUpdateOrganizationIdErrorComponent
                | ApiV1KubernetesControlplanesUpdateParentGatewayNameErrorComponent
                | ApiV1KubernetesControlplanesUpdateParentGatewayNamespaceErrorComponent
                | ApiV1KubernetesControlplanesUpdateParentGatewaySectionNameErrorComponent
                | ApiV1KubernetesControlplanesUpdatePersistenceSizeErrorComponent
                | ApiV1KubernetesControlplanesUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesControlplanesUpdateProviderErrorComponent
                | ApiV1KubernetesControlplanesUpdateProviderIdErrorComponent
                | ApiV1KubernetesControlplanesUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesControlplanesUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesControlplanesUpdateRegionIdErrorComponent
                | ApiV1KubernetesControlplanesUpdateScopeErrorComponent
                | ApiV1KubernetesControlplanesUpdateSecretsEncryptionEnabledErrorComponent
                | ApiV1KubernetesControlplanesUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesUpdateSlaTargetErrorComponent
                | ApiV1KubernetesControlplanesUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesUpdateSloTargetErrorComponent
                | ApiV1KubernetesControlplanesUpdateStorageClassErrorComponent
                | ApiV1KubernetesControlplanesUpdateTargetAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_0 = (
                        ApiV1KubernetesControlplanesUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_1 = (
                        ApiV1KubernetesControlplanesUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_2 = (
                        ApiV1KubernetesControlplanesUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_3 = (
                        ApiV1KubernetesControlplanesUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_4 = (
                        ApiV1KubernetesControlplanesUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_5 = (
                        ApiV1KubernetesControlplanesUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_6 = (
                        ApiV1KubernetesControlplanesUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_7 = (
                        ApiV1KubernetesControlplanesUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_8 = (
                        ApiV1KubernetesControlplanesUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_9 = (
                        ApiV1KubernetesControlplanesUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_10 = (
                        ApiV1KubernetesControlplanesUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_11 = (
                        ApiV1KubernetesControlplanesUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_12 = (
                        ApiV1KubernetesControlplanesUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_13 = (
                        ApiV1KubernetesControlplanesUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_14 = (
                        ApiV1KubernetesControlplanesUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_15 = (
                        ApiV1KubernetesControlplanesUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_16 = (
                        ApiV1KubernetesControlplanesUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_17 = (
                        ApiV1KubernetesControlplanesUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_18 = (
                        ApiV1KubernetesControlplanesUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_19 = (
                        ApiV1KubernetesControlplanesUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_20 = (
                        ApiV1KubernetesControlplanesUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_21 = (
                        ApiV1KubernetesControlplanesUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_22 = (
                        ApiV1KubernetesControlplanesUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_23 = (
                        ApiV1KubernetesControlplanesUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_24 = (
                        ApiV1KubernetesControlplanesUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_25 = (
                        ApiV1KubernetesControlplanesUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_26 = (
                        ApiV1KubernetesControlplanesUpdateRegionIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_27 = (
                        ApiV1KubernetesControlplanesUpdateLoadbalancerModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_28 = (
                        ApiV1KubernetesControlplanesUpdateLoadbalancerProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_29 = (
                        ApiV1KubernetesControlplanesUpdateExposureTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_30 = (
                        ApiV1KubernetesControlplanesUpdateParentGatewayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_31 = (
                        ApiV1KubernetesControlplanesUpdateParentGatewayNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_32 = (
                        ApiV1KubernetesControlplanesUpdateParentGatewaySectionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_33 = (
                        ApiV1KubernetesControlplanesUpdateGatewayClassNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_34 = (
                        ApiV1KubernetesControlplanesUpdateAuditLoggingEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_35 = (
                        ApiV1KubernetesControlplanesUpdateSecretsEncryptionEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_36 = (
                        ApiV1KubernetesControlplanesUpdateStorageClassErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_37 = (
                        ApiV1KubernetesControlplanesUpdatePersistenceSizeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_38 = (
                    ApiV1KubernetesControlplanesUpdateClusterDomainErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_controlplanes_update_error_type_38

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_controlplanes_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_controlplanes_update_validation_error.additional_properties = d
        return api_v1_kubernetes_controlplanes_update_validation_error

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
