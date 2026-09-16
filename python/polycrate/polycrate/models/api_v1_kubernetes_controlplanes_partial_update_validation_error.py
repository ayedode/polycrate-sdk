from __future__ import annotations

from collections.abc import Mapping
from typing import TYPE_CHECKING, Any, TypeVar

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.validation_error_enum import ValidationErrorEnum, check_validation_error_enum

if TYPE_CHECKING:
    from ..models.api_v1_kubernetes_controlplanes_partial_update_actual_availability_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateActualAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_annotations_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateAnnotationsErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_archived_at_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateArchivedAtErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_archived_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateArchivedErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_archived_reason_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateArchivedReasonErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_audit_logging_enabled_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateAuditLoggingEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_cluster_domain_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateClusterDomainErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_criticality_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateCriticalityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_debug_mode_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateDebugModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_discovery_enabled_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateDiscoveryEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_display_name_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateDisplayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_exposure_type_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateExposureTypeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_gateway_class_name_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateGatewayClassNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_kind_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateKindErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_labels_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateLabelsErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_loadbalancer_mode_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateLoadbalancerModeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_loadbalancer_provider_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateLoadbalancerProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_name_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_non_field_errors_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateNonFieldErrorsErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_organization_id_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateOrganizationIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_parent_gateway_name_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateParentGatewayNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_parent_gateway_namespace_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateParentGatewayNamespaceErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_parent_gateway_section_name_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateParentGatewaySectionNameErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_persistence_size_error_component import (
        ApiV1KubernetesControlplanesPartialUpdatePersistenceSizeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_platform_service_error_component import (
        ApiV1KubernetesControlplanesPartialUpdatePlatformServiceErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_provider_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateProviderErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_provider_id_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateProviderIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_provider_reference_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateProviderReferenceErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_reconciliation_enabled_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateReconciliationEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_region_id_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateRegionIdErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_scope_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateScopeErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_secrets_encryption_enabled_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateSecretsEncryptionEnabledErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_sla_availability_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateSlaAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_sla_target_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateSlaTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_slo_availability_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateSloAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_slo_target_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateSloTargetErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_storage_class_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateStorageClassErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_target_availability_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateTargetAvailabilityErrorComponent,
    )
    from ..models.api_v1_kubernetes_controlplanes_partial_update_workspace_id_error_component import (
        ApiV1KubernetesControlplanesPartialUpdateWorkspaceIdErrorComponent,
    )


T = TypeVar("T", bound="ApiV1KubernetesControlplanesPartialUpdateValidationError")


@_attrs_define
class ApiV1KubernetesControlplanesPartialUpdateValidationError:
    """
    Attributes:
        type_ (ValidationErrorEnum): * `validation_error` - Validation Error
        errors (list[ApiV1KubernetesControlplanesPartialUpdateActualAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateAnnotationsErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateArchivedAtErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateArchivedErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateArchivedReasonErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateAuditLoggingEnabledErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateClusterDomainErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateCriticalityErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateDebugModeErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateDiscoveryEnabledErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateDisplayNameErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateExposureTypeErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateGatewayClassNameErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateKindErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateLabelsErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateLoadbalancerModeErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateLoadbalancerProviderErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateNameErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateNonFieldErrorsErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateOrganizationIdErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateParentGatewayNameErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateParentGatewayNamespaceErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateParentGatewaySectionNameErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdatePersistenceSizeErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdatePlatformServiceErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateProviderErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateProviderIdErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateProviderReferenceErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateReconciliationEnabledErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateRegionIdErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateScopeErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateSecretsEncryptionEnabledErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateSlaAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateSlaTargetErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateSloAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateSloTargetErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateStorageClassErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateTargetAvailabilityErrorComponent |
            ApiV1KubernetesControlplanesPartialUpdateWorkspaceIdErrorComponent]):
    """

    type_: ValidationErrorEnum
    errors: list[
        ApiV1KubernetesControlplanesPartialUpdateActualAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateAnnotationsErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateArchivedAtErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateArchivedErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateArchivedReasonErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateAuditLoggingEnabledErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateClusterDomainErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateCriticalityErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateDebugModeErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateDiscoveryEnabledErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateDisplayNameErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateExposureTypeErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateGatewayClassNameErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateKindErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateLabelsErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateLoadbalancerModeErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateLoadbalancerProviderErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateNameErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateNonFieldErrorsErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateOrganizationIdErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateParentGatewayNameErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateParentGatewayNamespaceErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateParentGatewaySectionNameErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdatePersistenceSizeErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdatePlatformServiceErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateProviderErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateProviderIdErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateProviderReferenceErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateReconciliationEnabledErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateRegionIdErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateScopeErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateSecretsEncryptionEnabledErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateSlaAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateSlaTargetErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateSloAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateSloTargetErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateStorageClassErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateTargetAvailabilityErrorComponent
        | ApiV1KubernetesControlplanesPartialUpdateWorkspaceIdErrorComponent
    ]
    additional_properties: dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> dict[str, Any]:
        from ..models.api_v1_kubernetes_controlplanes_partial_update_actual_availability_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_annotations_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_archived_at_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_archived_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_archived_reason_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_audit_logging_enabled_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateAuditLoggingEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_criticality_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_debug_mode_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_display_name_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_exposure_type_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateExposureTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_gateway_class_name_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateGatewayClassNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_kind_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_labels_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_loadbalancer_mode_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateLoadbalancerModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_loadbalancer_provider_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateLoadbalancerProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_name_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_organization_id_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_parent_gateway_name_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateParentGatewayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_parent_gateway_namespace_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateParentGatewayNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_parent_gateway_section_name_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateParentGatewaySectionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_persistence_size_error_component import (
            ApiV1KubernetesControlplanesPartialUpdatePersistenceSizeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_platform_service_error_component import (
            ApiV1KubernetesControlplanesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_provider_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_provider_id_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_provider_reference_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_region_id_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateRegionIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_scope_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_secrets_encryption_enabled_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateSecretsEncryptionEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_sla_availability_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_sla_target_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_slo_availability_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_slo_target_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_storage_class_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateStorageClassErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_target_availability_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_workspace_id_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        type_: str = self.type_

        errors = []
        for errors_item_data in self.errors:
            errors_item: dict[str, Any]
            if isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateNonFieldErrorsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateDisplayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateLabelsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateAnnotationsErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateDebugModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateProviderErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateProviderReferenceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateProviderIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesControlplanesPartialUpdateReconciliationEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateDiscoveryEnabledErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdatePlatformServiceErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateScopeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateKindErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateArchivedErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateArchivedAtErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateArchivedReasonErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateCriticalityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesControlplanesPartialUpdateTargetAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesControlplanesPartialUpdateActualAvailabilityErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateSloTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateSloAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateSlaTargetErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateSlaAvailabilityErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateOrganizationIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateWorkspaceIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateRegionIdErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateLoadbalancerModeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesControlplanesPartialUpdateLoadbalancerProviderErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateExposureTypeErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateParentGatewayNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesControlplanesPartialUpdateParentGatewayNamespaceErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesControlplanesPartialUpdateParentGatewaySectionNameErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateGatewayClassNameErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesControlplanesPartialUpdateAuditLoggingEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(
                errors_item_data, ApiV1KubernetesControlplanesPartialUpdateSecretsEncryptionEnabledErrorComponent
            ):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdateStorageClassErrorComponent):
                errors_item = errors_item_data.to_dict()
            elif isinstance(errors_item_data, ApiV1KubernetesControlplanesPartialUpdatePersistenceSizeErrorComponent):
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
        from ..models.api_v1_kubernetes_controlplanes_partial_update_actual_availability_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateActualAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_annotations_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateAnnotationsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_archived_at_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateArchivedAtErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_archived_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateArchivedErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_archived_reason_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateArchivedReasonErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_audit_logging_enabled_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateAuditLoggingEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_cluster_domain_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateClusterDomainErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_criticality_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateCriticalityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_debug_mode_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateDebugModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_discovery_enabled_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateDiscoveryEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_display_name_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateDisplayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_exposure_type_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateExposureTypeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_gateway_class_name_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateGatewayClassNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_kind_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateKindErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_labels_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateLabelsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_loadbalancer_mode_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateLoadbalancerModeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_loadbalancer_provider_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateLoadbalancerProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_name_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_non_field_errors_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateNonFieldErrorsErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_organization_id_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateOrganizationIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_parent_gateway_name_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateParentGatewayNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_parent_gateway_namespace_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateParentGatewayNamespaceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_parent_gateway_section_name_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateParentGatewaySectionNameErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_persistence_size_error_component import (
            ApiV1KubernetesControlplanesPartialUpdatePersistenceSizeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_platform_service_error_component import (
            ApiV1KubernetesControlplanesPartialUpdatePlatformServiceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_provider_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateProviderErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_provider_id_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateProviderIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_provider_reference_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateProviderReferenceErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_reconciliation_enabled_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateReconciliationEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_region_id_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateRegionIdErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_scope_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateScopeErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_secrets_encryption_enabled_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateSecretsEncryptionEnabledErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_sla_availability_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateSlaAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_sla_target_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateSlaTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_slo_availability_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateSloAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_slo_target_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateSloTargetErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_storage_class_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateStorageClassErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_target_availability_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateTargetAvailabilityErrorComponent,  # noqa: PLC0415
        )
        from ..models.api_v1_kubernetes_controlplanes_partial_update_workspace_id_error_component import (
            ApiV1KubernetesControlplanesPartialUpdateWorkspaceIdErrorComponent,  # noqa: PLC0415
        )

        d = dict(src_dict)
        type_ = check_validation_error_enum(d.pop("type"))

        errors = []
        _errors = d.pop("errors")
        for errors_item_data in _errors:

            def _parse_errors_item(
                data: object,
            ) -> (
                ApiV1KubernetesControlplanesPartialUpdateActualAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateAnnotationsErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateArchivedAtErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateArchivedErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateArchivedReasonErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateAuditLoggingEnabledErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateClusterDomainErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateCriticalityErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateDebugModeErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateDiscoveryEnabledErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateDisplayNameErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateExposureTypeErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateGatewayClassNameErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateKindErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateLabelsErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateLoadbalancerModeErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateLoadbalancerProviderErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateNameErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateNonFieldErrorsErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateOrganizationIdErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateParentGatewayNameErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateParentGatewayNamespaceErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateParentGatewaySectionNameErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdatePersistenceSizeErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdatePlatformServiceErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateProviderErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateProviderIdErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateProviderReferenceErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateReconciliationEnabledErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateRegionIdErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateScopeErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateSecretsEncryptionEnabledErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateSlaAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateSlaTargetErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateSloAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateSloTargetErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateStorageClassErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateTargetAvailabilityErrorComponent
                | ApiV1KubernetesControlplanesPartialUpdateWorkspaceIdErrorComponent
            ):
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_0 = (
                        ApiV1KubernetesControlplanesPartialUpdateNonFieldErrorsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_0
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_1 = (
                        ApiV1KubernetesControlplanesPartialUpdateNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_1
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_2 = (
                        ApiV1KubernetesControlplanesPartialUpdateDisplayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_2
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_3 = (
                        ApiV1KubernetesControlplanesPartialUpdateLabelsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_3
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_4 = (
                        ApiV1KubernetesControlplanesPartialUpdateAnnotationsErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_4
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_5 = (
                        ApiV1KubernetesControlplanesPartialUpdateDebugModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_5
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_6 = (
                        ApiV1KubernetesControlplanesPartialUpdateProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_6
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_7 = (
                        ApiV1KubernetesControlplanesPartialUpdateProviderReferenceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_7
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_8 = (
                        ApiV1KubernetesControlplanesPartialUpdateProviderIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_8
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_9 = (
                        ApiV1KubernetesControlplanesPartialUpdateReconciliationEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_9
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_10 = (
                        ApiV1KubernetesControlplanesPartialUpdateDiscoveryEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_10
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_11 = (
                        ApiV1KubernetesControlplanesPartialUpdatePlatformServiceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_11
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_12 = (
                        ApiV1KubernetesControlplanesPartialUpdateScopeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_12
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_13 = (
                        ApiV1KubernetesControlplanesPartialUpdateKindErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_13
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_14 = (
                        ApiV1KubernetesControlplanesPartialUpdateArchivedErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_14
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_15 = (
                        ApiV1KubernetesControlplanesPartialUpdateArchivedAtErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_15
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_16 = (
                        ApiV1KubernetesControlplanesPartialUpdateArchivedReasonErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_16
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_17 = (
                        ApiV1KubernetesControlplanesPartialUpdateCriticalityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_17
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_18 = (
                        ApiV1KubernetesControlplanesPartialUpdateTargetAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_18
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_19 = (
                        ApiV1KubernetesControlplanesPartialUpdateActualAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_19
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_20 = (
                        ApiV1KubernetesControlplanesPartialUpdateSloTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_20
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_21 = (
                        ApiV1KubernetesControlplanesPartialUpdateSloAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_21
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_22 = (
                        ApiV1KubernetesControlplanesPartialUpdateSlaTargetErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_22
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_23 = (
                        ApiV1KubernetesControlplanesPartialUpdateSlaAvailabilityErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_23
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_24 = (
                        ApiV1KubernetesControlplanesPartialUpdateOrganizationIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_24
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_25 = (
                        ApiV1KubernetesControlplanesPartialUpdateWorkspaceIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_25
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_26 = (
                        ApiV1KubernetesControlplanesPartialUpdateRegionIdErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_26
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_27 = (
                        ApiV1KubernetesControlplanesPartialUpdateLoadbalancerModeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_27
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_28 = (
                        ApiV1KubernetesControlplanesPartialUpdateLoadbalancerProviderErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_28
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_29 = (
                        ApiV1KubernetesControlplanesPartialUpdateExposureTypeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_29
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_30 = (
                        ApiV1KubernetesControlplanesPartialUpdateParentGatewayNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_30
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_31 = (
                        ApiV1KubernetesControlplanesPartialUpdateParentGatewayNamespaceErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_31
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_32 = (
                        ApiV1KubernetesControlplanesPartialUpdateParentGatewaySectionNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_32
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_33 = (
                        ApiV1KubernetesControlplanesPartialUpdateGatewayClassNameErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_33
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_34 = (
                        ApiV1KubernetesControlplanesPartialUpdateAuditLoggingEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_34
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_35 = (
                        ApiV1KubernetesControlplanesPartialUpdateSecretsEncryptionEnabledErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_35
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_36 = (
                        ApiV1KubernetesControlplanesPartialUpdateStorageClassErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_36
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                try:
                    if not isinstance(data, dict):
                        raise TypeError()
                    componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_37 = (
                        ApiV1KubernetesControlplanesPartialUpdatePersistenceSizeErrorComponent.from_dict(data)
                    )

                    return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_37
                except (TypeError, ValueError, AttributeError, KeyError):
                    pass
                if not isinstance(data, dict):
                    raise TypeError()
                componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_38 = (
                    ApiV1KubernetesControlplanesPartialUpdateClusterDomainErrorComponent.from_dict(data)
                )

                return componentsschemas_api_v1_kubernetes_controlplanes_partial_update_error_type_38

            errors_item = _parse_errors_item(errors_item_data)

            errors.append(errors_item)

        api_v1_kubernetes_controlplanes_partial_update_validation_error = cls(
            type_=type_,
            errors=errors,
        )

        api_v1_kubernetes_controlplanes_partial_update_validation_error.additional_properties = d
        return api_v1_kubernetes_controlplanes_partial_update_validation_error

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
