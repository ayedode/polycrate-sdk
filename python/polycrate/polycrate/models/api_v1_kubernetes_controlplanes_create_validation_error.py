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
    from ..models.api_v1_kubernetes_controlplanes_create_audit_logging_enabled_error_component import (
        ApiV1KubernetesControlplanesCreateAuditLoggingEnabledErrorComponent,
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
    from ..models.api_v1_kubernetes_controlplanes_create_exposure_type_error_component import (
        ApiV1KubernetesControlplanesCreateExposureTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_gateway_class_name_error_component import (
        ApiV1KubernetesControlplanesCreateGatewayClassNameErrorComponent,
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
    from ..models.api_v1_kubernetes_controlplanes_create_organization_id_error_component import (
        ApiV1KubernetesControlplanesCreateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_parent_gateway_name_error_component import (
        ApiV1KubernetesControlplanesCreateParentGatewayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_parent_gateway_namespace_error_component import (
        ApiV1KubernetesControlplanesCreateParentGatewayNamespaceErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_parent_gateway_section_name_error_component import (
        ApiV1KubernetesControlplanesCreateParentGatewaySectionNameErrorComponent,
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
    from ..models.api_v1_kubernetes_controlplanes_create_region_id_error_component import (
        ApiV1KubernetesControlplanesCreateRegionIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_scope_error_component import (
        ApiV1KubernetesControlplanesCreateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_create_secrets_encryption_enabled_error_component import (
        ApiV1KubernetesControlplanesCreateSecretsEncryptionEnabledErrorComponent,
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
    from ..models.api_v1_kubernetes_controlplanes_create_workspace_id_error_component import (
        ApiV1KubernetesControlplanesCreateWorkspaceIdErrorComponent,
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
            ApiV1KubernetesControlplanesCreateAuditLoggingEnabledErrorComponent |
            ApiV1KubernetesControlplanesCreateClusterDomainErrorComponent |
            ApiV1KubernetesControlplanesCreateCriticalityErrorComponent |
            ApiV1KubernetesControlplanesCreateDebugModeErrorComponent |
            ApiV1KubernetesControlplanesCreateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesControlplanesCreateDisplayNameErrorComponent |
            ApiV1KubernetesControlplanesCreateExposureTypeErrorComponent |
            ApiV1KubernetesControlplanesCreateGatewayClassNameErrorComponent |
            ApiV1KubernetesControlplanesCreateKindErrorComponent | ApiV1KubernetesControlplanesCreateLabelsErrorComponent |
            ApiV1KubernetesControlplanesCreateLoadbalancerModeErrorComponent |
            ApiV1KubernetesControlplanesCreateLoadbalancerProviderErrorComponent |
            ApiV1KubernetesControlplanesCreateNameErrorComponent |
            ApiV1KubernetesControlplanesCreateNonFieldErrorsErrorComponent |
            ApiV1KubernetesControlplanesCreateOrganizationIdErrorComponent |
            ApiV1KubernetesControlplanesCreateParentGatewayNameErrorComponent |
            ApiV1KubernetesControlplanesCreateParentGatewayNamespaceErrorComponent |
            ApiV1KubernetesControlplanesCreateParentGatewaySectionNameErrorComponent |
            ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponent |
            ApiV1KubernetesControlplanesCreatePlatformServiceErrorComponent |
            ApiV1KubernetesControlplanesCreateProviderErrorComponent |
            ApiV1KubernetesControlplanesCreateProviderIdErrorComponent |
            ApiV1KubernetesControlplanesCreateProviderReferenceErrorComponent |
            ApiV1KubernetesControlplanesCreateReconciliationEnabledErrorComponent |
            ApiV1KubernetesControlplanesCreateRegionIdErrorComponent | ApiV1KubernetesControlplanesCreateScopeErrorComponent
            | ApiV1KubernetesControlplanesCreateSecretsEncryptionEnabledErrorComponent |
            ApiV1KubernetesControlplanesCreateSlaAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesCreateSlaTargetErrorComponent |
            ApiV1KubernetesControlplanesCreateSloAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesCreateSloTargetErrorComponent |
            ApiV1KubernetesControlplanesCreateStorageClassErrorComponent |
            ApiV1KubernetesControlplanesCreateTargetAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesCreateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesControlplanesCreateActualAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesCreateAnnotationsErrorComponent
        | ApiV1KubernetesControlplanesCreateArchivedAtErrorComponent
        | ApiV1KubernetesControlplanesCreateArchivedErrorComponent
        | ApiV1KubernetesControlplanesCreateArchivedReasonErrorComponent
        | ApiV1KubernetesControlplanesCreateAuditLoggingEnabledErrorComponent
        | ApiV1KubernetesControlplanesCreateClusterDomainErrorComponent
        | ApiV1KubernetesControlplanesCreateCriticalityErrorComponent
        | ApiV1KubernetesControlplanesCreateDebugModeErrorComponent
        | ApiV1KubernetesControlplanesCreateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesControlplanesCreateDisplayNameErrorComponent
        | ApiV1KubernetesControlplanesCreateExposureTypeErrorComponent
        | ApiV1KubernetesControlplanesCreateGatewayClassNameErrorComponent
        | ApiV1KubernetesControlplanesCreateKindErrorComponent
        | ApiV1KubernetesControlplanesCreateLabelsErrorComponent
        | ApiV1KubernetesControlplanesCreateLoadbalancerModeErrorComponent
        | ApiV1KubernetesControlplanesCreateLoadbalancerProviderErrorComponent
        | ApiV1KubernetesControlplanesCreateNameErrorComponent
        | ApiV1KubernetesControlplanesCreateNonFieldErrorsErrorComponent
        | ApiV1KubernetesControlplanesCreateOrganizationIdErrorComponent
        | ApiV1KubernetesControlplanesCreateParentGatewayNameErrorComponent
        | ApiV1KubernetesControlplanesCreateParentGatewayNamespaceErrorComponent
        | ApiV1KubernetesControlplanesCreateParentGatewaySectionNameErrorComponent
        | ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponent
        | ApiV1KubernetesControlplanesCreatePlatformServiceErrorComponent
        | ApiV1KubernetesControlplanesCreateProviderErrorComponent
        | ApiV1KubernetesControlplanesCreateProviderIdErrorComponent
        | ApiV1KubernetesControlplanesCreateProviderReferenceErrorComponent
        | ApiV1KubernetesControlplanesCreateReconciliationEnabledErrorComponent
        | ApiV1KubernetesControlplanesCreateRegionIdErrorComponent
        | ApiV1KubernetesControlplanesCreateScopeErrorComponent
        | ApiV1KubernetesControlplanesCreateSecretsEncryptionEnabledErrorComponent
        | ApiV1KubernetesControlplanesCreateSlaAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesCreateSlaTargetErrorComponent
        | ApiV1KubernetesControlplanesCreateSloAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesCreateSloTargetErrorComponent
        | ApiV1KubernetesControlplanesCreateStorageClassErrorComponent
        | ApiV1KubernetesControlplanesCreateTargetAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesCreateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_controlplanes_create_actual_availability_error_component import (
            ApiV1KubernetesControlplanesCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_annotations_error_component import (
            ApiV1KubernetesControlplanesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_archived_at_error_component import (
            ApiV1KubernetesControlplanesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_archived_error_component import (
            ApiV1KubernetesControlplanesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_archived_reason_error_component import (
            ApiV1KubernetesControlplanesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_audit_logging_enabled_error_component import (
            ApiV1KubernetesControlplanesCreateAuditLoggingEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_criticality_error_component import (
            ApiV1KubernetesControlplanesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_debug_mode_error_component import (
            ApiV1KubernetesControlplanesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_discovery_enabled_error_component import (
            ApiV1KubernetesControlplanesCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_display_name_error_component import (
            ApiV1KubernetesControlplanesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_exposure_type_error_component import (
            ApiV1KubernetesControlplanesCreateExposureTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_gateway_class_name_error_component import (
            ApiV1KubernetesControlplanesCreateGatewayClassNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_kind_error_component import (
            ApiV1KubernetesControlplanesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_labels_error_component import (
            ApiV1KubernetesControlplanesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_loadbalancer_mode_error_component import (
            ApiV1KubernetesControlplanesCreateLoadbalancerModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_loadbalancer_provider_error_component import (
            ApiV1KubernetesControlplanesCreateLoadbalancerProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_name_error_component import (
            ApiV1KubernetesControlplanesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_non_field_errors_error_component import (
            ApiV1KubernetesControlplanesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_organization_id_error_component import (
            ApiV1KubernetesControlplanesCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_parent_gateway_name_error_component import (
            ApiV1KubernetesControlplanesCreateParentGatewayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_parent_gateway_namespace_error_component import (
            ApiV1KubernetesControlplanesCreateParentGatewayNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_parent_gateway_section_name_error_component import (
            ApiV1KubernetesControlplanesCreateParentGatewaySectionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_persistence_size_error_component import (
            ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_platform_service_error_component import (
            ApiV1KubernetesControlplanesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_provider_error_component import (
            ApiV1KubernetesControlplanesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_provider_id_error_component import (
            ApiV1KubernetesControlplanesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_provider_reference_error_component import (
            ApiV1KubernetesControlplanesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesControlplanesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_region_id_error_component import (
            ApiV1KubernetesControlplanesCreateRegionIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_scope_error_component import (
            ApiV1KubernetesControlplanesCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_secrets_encryption_enabled_error_component import (
            ApiV1KubernetesControlplanesCreateSecretsEncryptionEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_sla_availability_error_component import (
            ApiV1KubernetesControlplanesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_sla_target_error_component import (
            ApiV1KubernetesControlplanesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_slo_availability_error_component import (
            ApiV1KubernetesControlplanesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_slo_target_error_component import (
            ApiV1KubernetesControlplanesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_storage_class_error_component import (
            ApiV1KubernetesControlplanesCreateStorageClassErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_target_availability_error_component import (
            ApiV1KubernetesControlplanesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_workspace_id_error_component import (
            ApiV1KubernetesControlplanesCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
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
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateRegionIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateLoadbalancerModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateLoadbalancerProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateExposureTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateParentGatewayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateParentGatewayNamespaceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateParentGatewaySectionNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateGatewayClassNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateAuditLoggingEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesCreateSecretsEncryptionEnabledErrorComponent):
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
            ApiV1KubernetesControlplanesCreateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_annotations_error_component import (
            ApiV1KubernetesControlplanesCreateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_archived_at_error_component import (
            ApiV1KubernetesControlplanesCreateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_archived_error_component import (
            ApiV1KubernetesControlplanesCreateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_archived_reason_error_component import (
            ApiV1KubernetesControlplanesCreateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_audit_logging_enabled_error_component import (
            ApiV1KubernetesControlplanesCreateAuditLoggingEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_cluster_domain_error_component import (
            ApiV1KubernetesControlplanesCreateClusterDomainErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_criticality_error_component import (
            ApiV1KubernetesControlplanesCreateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_debug_mode_error_component import (
            ApiV1KubernetesControlplanesCreateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_discovery_enabled_error_component import (
            ApiV1KubernetesControlplanesCreateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_display_name_error_component import (
            ApiV1KubernetesControlplanesCreateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_exposure_type_error_component import (
            ApiV1KubernetesControlplanesCreateExposureTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_gateway_class_name_error_component import (
            ApiV1KubernetesControlplanesCreateGatewayClassNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_kind_error_component import (
            ApiV1KubernetesControlplanesCreateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_labels_error_component import (
            ApiV1KubernetesControlplanesCreateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_loadbalancer_mode_error_component import (
            ApiV1KubernetesControlplanesCreateLoadbalancerModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_loadbalancer_provider_error_component import (
            ApiV1KubernetesControlplanesCreateLoadbalancerProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_name_error_component import (
            ApiV1KubernetesControlplanesCreateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_non_field_errors_error_component import (
            ApiV1KubernetesControlplanesCreateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_organization_id_error_component import (
            ApiV1KubernetesControlplanesCreateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_parent_gateway_name_error_component import (
            ApiV1KubernetesControlplanesCreateParentGatewayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_parent_gateway_namespace_error_component import (
            ApiV1KubernetesControlplanesCreateParentGatewayNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_parent_gateway_section_name_error_component import (
            ApiV1KubernetesControlplanesCreateParentGatewaySectionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_persistence_size_error_component import (
            ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_platform_service_error_component import (
            ApiV1KubernetesControlplanesCreatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_provider_error_component import (
            ApiV1KubernetesControlplanesCreateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_provider_id_error_component import (
            ApiV1KubernetesControlplanesCreateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_provider_reference_error_component import (
            ApiV1KubernetesControlplanesCreateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_reconciliation_enabled_error_component import (
            ApiV1KubernetesControlplanesCreateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_region_id_error_component import (
            ApiV1KubernetesControlplanesCreateRegionIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_scope_error_component import (
            ApiV1KubernetesControlplanesCreateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_secrets_encryption_enabled_error_component import (
            ApiV1KubernetesControlplanesCreateSecretsEncryptionEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_sla_availability_error_component import (
            ApiV1KubernetesControlplanesCreateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_sla_target_error_component import (
            ApiV1KubernetesControlplanesCreateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_slo_availability_error_component import (
            ApiV1KubernetesControlplanesCreateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_slo_target_error_component import (
            ApiV1KubernetesControlplanesCreateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_storage_class_error_component import (
            ApiV1KubernetesControlplanesCreateStorageClassErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_target_availability_error_component import (
            ApiV1KubernetesControlplanesCreateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_create_workspace_id_error_component import (
            ApiV1KubernetesControlplanesCreateWorkspaceIdErrorComponent,  # noqa: PLC0415
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
                | ApiV1KubernetesControlplanesCreateAuditLoggingEnabledErrorComponent
                | ApiV1KubernetesControlplanesCreateClusterDomainErrorComponent
                | ApiV1KubernetesControlplanesCreateCriticalityErrorComponent
                | ApiV1KubernetesControlplanesCreateDebugModeErrorComponent
                | ApiV1KubernetesControlplanesCreateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesControlplanesCreateDisplayNameErrorComponent
                | ApiV1KubernetesControlplanesCreateExposureTypeErrorComponent
                | ApiV1KubernetesControlplanesCreateGatewayClassNameErrorComponent
                | ApiV1KubernetesControlplanesCreateKindErrorComponent
                | ApiV1KubernetesControlplanesCreateLabelsErrorComponent
                | ApiV1KubernetesControlplanesCreateLoadbalancerModeErrorComponent
                | ApiV1KubernetesControlplanesCreateLoadbalancerProviderErrorComponent
                | ApiV1KubernetesControlplanesCreateNameErrorComponent
                | ApiV1KubernetesControlplanesCreateNonFieldErrorsErrorComponent
                | ApiV1KubernetesControlplanesCreateOrganizationIdErrorComponent
                | ApiV1KubernetesControlplanesCreateParentGatewayNameErrorComponent
                | ApiV1KubernetesControlplanesCreateParentGatewayNamespaceErrorComponent
                | ApiV1KubernetesControlplanesCreateParentGatewaySectionNameErrorComponent
                | ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponent
                | ApiV1KubernetesControlplanesCreatePlatformServiceErrorComponent
                | ApiV1KubernetesControlplanesCreateProviderErrorComponent
                | ApiV1KubernetesControlplanesCreateProviderIdErrorComponent
                | ApiV1KubernetesControlplanesCreateProviderReferenceErrorComponent
                | ApiV1KubernetesControlplanesCreateReconciliationEnabledErrorComponent
                | ApiV1KubernetesControlplanesCreateRegionIdErrorComponent
                | ApiV1KubernetesControlplanesCreateScopeErrorComponent
                | ApiV1KubernetesControlplanesCreateSecretsEncryptionEnabledErrorComponent
                | ApiV1KubernetesControlplanesCreateSlaAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesCreateSlaTargetErrorComponent
                | ApiV1KubernetesControlplanesCreateSloAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesCreateSloTargetErrorComponent
                | ApiV1KubernetesControlplanesCreateStorageClassErrorComponent
                | ApiV1KubernetesControlplanesCreateTargetAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesCreateWorkspaceIdErrorComponent
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
                        ApiV1KubernetesControlplanesCreateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_25 = (
                        ApiV1KubernetesControlplanesCreateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_26 = (
                        ApiV1KubernetesControlplanesCreateRegionIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_27 = (
                        ApiV1KubernetesControlplanesCreateLoadbalancerModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_28 = (
                        ApiV1KubernetesControlplanesCreateLoadbalancerProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_29 = (
                        ApiV1KubernetesControlplanesCreateExposureTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_30 = (
                        ApiV1KubernetesControlplanesCreateParentGatewayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_31 = (
                        ApiV1KubernetesControlplanesCreateParentGatewayNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_32 = (
                        ApiV1KubernetesControlplanesCreateParentGatewaySectionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_33 = (
                        ApiV1KubernetesControlplanesCreateGatewayClassNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_34 = (
                        ApiV1KubernetesControlplanesCreateAuditLoggingEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_35 = (
                        ApiV1KubernetesControlplanesCreateSecretsEncryptionEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_36 = (
                        ApiV1KubernetesControlplanesCreateStorageClassErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_37 = (
                        ApiV1KubernetesControlplanesCreatePersistenceSizeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_38 = (
                    ApiV1KubernetesControlplanesCreateClusterDomainErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_controlplanes_create_error_type_38

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
